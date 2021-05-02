package ir;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class SimilarityScore {

    public static void main(String[] args) throws IOException {

        ////////////////////////////////////////////////////////
        ///////// MUST CHANGE TO TEST OUT FUNCTIONALITY ////////
        ////////////////////////////////////////////////////////
        
        String project_path = "/Users/priyashah/Documents/NETS_150";
        
        ////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////

        /*
         * Parse Information
         */

        // get files
        File folder = new File(project_path);
        File[] fileList = folder.listFiles();

        Document currDoc = null;

        ArrayList<Document> documents = new ArrayList<Document>();
        ArrayList<Tuple> rankings = new ArrayList<Tuple>();

        // Create documents for text files
        for (File file : fileList) {
            if (file.isFile() && file.getName().contains(".txt")) {
                Document name = new Document(file.getName());
                documents.add(name);
            }
        }

        // Find current doc
        for (Document doc : documents) {
            if (doc.getFileName().contains(docName + ".txt")) {
                currDoc = doc;
                break;
            }
        }

        Corpus corpus = new Corpus(documents);

        VectorSpaceModel vectorSpace = new VectorSpaceModel(corpus);

        System.out.println("**************************************************");
        System.out.println("**************************************************");
        System.out.println("**************************************************");
        
        // get the similarity scores for each document
        for (Document doc : documents) {
            if (doc == currDoc) {
                continue;
            }
            double x = vectorSpace.cosineSimilarity(doc, currDoc);
            Tuple comparison = new Tuple(doc, x);
            rankings.add(comparison);
        }

        // go through the similarity scores and find the maximum
        double max = 0;
        Document mostSimilar = null;
        for (Tuple score : rankings) {
            System.out.println(score.getScore() + "   ,   " + score.getDocName());
            if (score.getScore() > max) {
                max = score.getScore();
                mostSimilar = score.getDocName();
            }
        }
        
        System.out.println("**************************************************");
        System.out.println("**************************************************");
        System.out.println("**************************************************");

        if (mostSimilar == null) {
            System.out.println("Sorry. There are not enough files in the system yet.");
        } else {
            System.out.println("You would be great friends with " + mostSimilar.getFileName().split(".txt")[0] + '!');
        }

    }

    // inner class to track (document, score) pairs
    static class Tuple {
        private Document documentName;
        private double similarityScore;

        private Tuple(Document docName, double d) {
            documentName = docName;
            similarityScore = d;
        }

        public Document getDocName() {
            return documentName;
        }

        public double getScore() {
            return similarityScore;
        }
    }

}
