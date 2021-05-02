import java.util.ArrayList;

public class VectorRanking {
    public static void main(String[] args) {
		
		String[] schools = new String[] {"CMU", "UIUC", "MIT", "stanford", "UCSD", "berkeley", "cornell", "umich", "udub", "umd", "gatech", 
		"neu", "columbia", "uwmadison", "upenn", "utaustin" , "purdue", "umass", "nyu", "ucla"};

		Document keywords = new Document("keywords.txt");

		ArrayList<Document> documents = new ArrayList<Document>();

		documents.add(keywords);

		for(int i = 0; i < schools.length; i++) {

			documents.add(new Document(schools[i] + ".txt"));

		}
		
		Corpus corpus = new Corpus(documents);
		
		VectorSpaceModel vectorSpace = new VectorSpaceModel(corpus);
		
		for(int i = 1; i < documents.size(); i++) {
			Document doc = documents.get(i);
			System.out.println("\nComparing to " + schools[i - 1]);
			System.out.println(vectorSpace.cosineSimilarity(keywords, doc));
		}
		
		
		
	}
}
