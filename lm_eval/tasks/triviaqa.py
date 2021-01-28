import os
import json
import random
from lm_eval.base import Dataset
from ..utils import sh

class TriviaQA(Dataset):
    def download(self):
        if not os.path.exists('data/triviaqa'):
            sh("""
            mkdir -p data/triviaqa
            wget http://nlp.cs.washington.edu/triviaqa/data/triviaqa-unfiltered.tar.gz -O data/triviaqa/trivia_qa-unfiltered.tar.gz
            tar -xf data/triviaqa/trivia_qa-unfiltered.tar.gz
            mv triviaqa-unfiltered/ data/triviaqa/
            """)

    def has_training_docs(self):
        return True

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return True

    def training_docs(self):
        return json.load(open('data/triviaqa/triviaqa-unfiltered/unfiltered-web-train.json'))['Data']

    def validation_docs(self):
        return  json.load(open('data/triviaqa/triviaqa-unfiltered/unfiltered-web-dev.json'))['Data']

    def test_docs(self):
        return  json.load(open('data/triviaqa/triviaqa-unfiltered/unfiltered-web-test.json'))['Data']     
    
    def fewshot_description(self):
        # TODO: figure out fewshot description
        return ""
    
    def doc_to_text(self, doc):
        return ''.join(['Q: ', doc['Question'], '\n\n','A: '])

    def doc_to_target(self, doc):
        return doc['Answer']['Aliases'][0]

    def construct_requests(self, doc, ctx):
        """ Uses RequestFactory to construct Requests and returns an iterable of 
        Requests which will be sent to the LM.

        :param doc:
            The document as returned from training_docs, validation_docs, or test_docs.
        :param ctx: str
            The context string, generated by fewshot_context. This includes the natural 
            language description, as well as the few shot examples, and the question
            part of the document for `doc`. 
        """
        # TODO: implement evaluation.
        raise NotImplementedError('Evaluation not implemented')
    
    def process_results(self, doc, results):
        """Take a single document and the LM results and evaluates, returning a 
        dict where keys are the names of submetrics and values are the values of 
        the metric for that one document

        :param doc:
            The document as returned from training_docs, validation_docs, or test_docs.
        :param results:
            The results of the requests created in construct_requests.
        """
        # TODO: implement evaluation.
        raise NotImplementedError('Evaluation not implemented')

    def aggregation(self):
        """
        :returns: {str: [float] -> float}
            A dictionary where keys are the names of submetrics and values are 
            functions that aggregate a list of metrics
        """
        # TODO: implement evaluation.
        raise NotImplementedError('Evaluation not implemented')

    def higher_is_better(self):
        """
        :returns: {str: bool}
            A dictionary where keys are the names of submetrics and values are 
            whether a higher value of the submetric is better
        """
        # TODO: implement evaluation.
        raise NotImplementedError('Evaluation not implemented')