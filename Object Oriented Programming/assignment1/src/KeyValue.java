import java.util.StringTokenizer;

public class KeyValue {

	private String key;
	private String value;
	
	
	public KeyValue(String properties) {
		
		StringTokenizer st = new StringTokenizer(properties, "=");
		this.key = st.nextToken();
		this.value = st.nextToken();
		
	}
	public KeyValue(String key, String value) {
		
		this.key = key;
		this.value = value;
		
	}
	public String getKey() {
		return key;
	}
	public String getValue() {
		return value;
	}
}
