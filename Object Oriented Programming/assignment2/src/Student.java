import java.util.*;

public class Student implements Voter{
	
	private String studentName;
	private int studentNumber;
	private Department studentDepartment;
	private int studentGrade;
	
	public String getStudentName() {
		return studentName;
	}
	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}
	public int getStudentNumber() {
		return studentNumber;
	}
	public void setStudentNumber(int studentNumber) {
		this.studentNumber = studentNumber;
	}
	public Department getStudentDepartment() {
		return studentDepartment;
	}
	public void setStudentDepartment(Department studentDepartment) {
		this.studentDepartment = studentDepartment;
	}
	public int getStudentGrade() {
		return studentGrade;
	}
	public void setStudentGrade(int studentGrade) {
		this.studentGrade = studentGrade;
	}
	
	public Student(int studentNumber, Department studentDepartment, String studentName) {
		this.studentNumber = studentNumber;
		this.studentDepartment = studentDepartment;
		this.studentName = studentName;
	}
	
	@Override
	public void vote() {
		Random random = new Random();
		int temp = random.nextInt(this.studentDepartment.candidate.size()-1);
		this.studentDepartment.candidate.get(temp).increase();
	}
	
	@Override
	public int compareTo(Object arg0) {
		// TODO Auto-generated method stub
		return 0;
	}
}
