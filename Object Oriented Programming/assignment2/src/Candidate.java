
public class Candidate extends Student{
	
	private int voteNumber;
	
	public int getVoteNumber() {
		return voteNumber;
	}

	public void setVoteNumber(int voteNumber) {
		this.voteNumber = voteNumber;
	}

	public void increase() {
		this.voteNumber++;
	} 
	public Candidate(int studentNumber, Department studentDepartment, String studentName, int voteNumber) {
		super(studentNumber, studentDepartment, studentName);
		this.voteNumber = voteNumber;
	}
	
	@Override
	public int compareTo(Object arg0) {
		
		Candidate tmp = (Candidate)arg0;
		if(this.voteNumber > tmp.voteNumber)	return 1;
		else if (this.voteNumber == tmp.voteNumber)	return 0;
		else return -1;
	}

	
	public String toString() {
		return 
				"======== Elected Candidate ========\n" + 
				"Department Name: " + super.getStudentDepartment().getDepartmentName() + "\n" +
				"name: " + super.getStudentName() + "\n" +
				"Student_id: "+ super.getStudentNumber() + "\n"+
				"Votes: "+ this.getVoteNumber() + "\n" +
				"===================================\n"
				;
		
	}
}
