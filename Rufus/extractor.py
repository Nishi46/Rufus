import spacy
from spacy.matcher import PhraseMatcher
from bs4 import BeautifulSoup
from Rufus.error_handler import ErrorHandler

class DataExtractor:
    def __init__(self, raw_data, instructions, similarity_threshold=0.7):
        self.raw_data = raw_data
        self.instructions = instructions
        self.similarity_threshold = similarity_threshold
        self.nlp = spacy.load("en_core_web_md")
        self.matcher = PhraseMatcher(self.nlp.vocab)
        self._prepare_phrase_matcher()

    def extract(self):
        """
        Extracts relevant content from the given raw_data based on the instructions.

        Args:
        - raw_data (list): a list of strings where each string is a page of text.
        - instructions (str): a string containing the instructions to extract relevant
          content.

        Returns:
        - dict: a dictionary with a single key "extracted_data" that contains a list
          of strings where each string is a relevant line extracted from the pages.
        """
        extracted_content = []
        try:
            for page in self.raw_data:
                soup = BeautifulSoup(page, 'html.parser')
                text_content = soup.get_text(separator="\n")
                doc_instructions = self.nlp(self.instructions.lower())
                relevant_lines = self._filter_content(text_content, doc_instructions)
                extracted_content.append(relevant_lines)
            return {"extracted_data": extracted_content}
        except Exception as e:
            ErrorHandler.handle_extraction_error(self.raw_data)
            raise RuntimeError("Data extraction failed") from e

    def _prepare_phrase_matcher(self):
        
        """
        Prepare a phrase matcher to filter relevant lines based on the instructions.

        The phrases are non-stop and non-punctuation words from the instructions.
        The matcher is then used to filter relevant lines from the given text content.
        """
        doc = self.nlp(self.instructions.lower())
        phrases = [token.text for token in doc if not token.is_stop and not token.is_punct]
        patterns = [self.nlp.make_doc(phrase) for phrase in phrases]
        self.matcher.add("instructions_matcher", None, *patterns)

    def _filter_content(self, text_content, doc_instructions):
        """
        Filter relevant lines from the given text content based on the instructions.

        Args:
            text_content (str): The text content to filter.
            doc_instructions (spacy.doc.Doc): The instructions to match against.

        Returns:
            List[str]: A list of sentences that match the instructions.
        """
        relevant_lines = []
        sentences = text_content.split("\n")
        for sentence in sentences:
            doc_sentence = self.nlp(sentence.lower())
            matches = self.matcher(doc_sentence)
            if matches:
                relevant_lines.append(sentence.strip())
                continue
            similarity = doc_instructions.similarity(doc_sentence)
            if similarity > self.similarity_threshold:
                relevant_lines.append(sentence.strip())
        return relevant_lines
