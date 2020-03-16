import java.util.ArrayList;

public class Department {
	
	private int departmentNumber;
	private String departmentName;
	ArrayList<Candidate> candidate = new ArrayList<Candidate>();
	ArrayList<Student> student = new ArrayList<Student>();
	
	public Department(int num, String dp) {
		this.departmentNumber = num;
		this.departmentName = dp;
	}
	
	public int getDepartmentNumber() {
		return departmentNumber;
	}
	public void setDepartmentNumber(int departmentNumber) {
		this.departmentNumber = departmentNumber;
	}
	public String getDepartmentName() {
		return departmentName;
	}
	public void setDepartmentName(String departmentName) {
		this.departmentName = departmentName;
	} 
	
	public Candidate mostVotes() {
		
		Candidate result = null;
		
		for(Candidate candidateTemp : candidate) {
			if(result == null)	result = candidateTemp;
			if(result.getVoteNumber()< candidateTemp.getVoteNumber())	result = candidateTemp;
		}
		
		return result;
	}
}
