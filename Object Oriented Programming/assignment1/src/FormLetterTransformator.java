import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FormLetterTransformator {

	public static void main(String[] args) {
		Scanner fileIn1 = null ;
		Scanner fileIn2 = null ;
		int i, j;
		int a = 9;	//template_file.txt의 줄수가 a
		
		try
		{
			fileIn1 = new Scanner( new FileInputStream("properties.txt"));
		}
		catch (FileNotFoundException e)
		{
			System.out.println("File not found.");
			System.exit(0);
		}
		try
		{
			fileIn2 = new Scanner( new FileInputStream("template_file.txt"));
		}
		catch (FileNotFoundException e)
		{
			System.out.println("File not found.");
			System.exit(0);
		}
		
		KeyValue[] prop = new KeyValue[6];
		
		for (i = 0; i < 6; i++) {
			prop[i] = new KeyValue(fileIn1.nextLine());
		}
		
		String[] temp = new String[a];	
		
		for (i = 0; i < a; i++) {
			temp[i] = fileIn2.nextLine();
		}
		
		String[] out = new String[a];
		
		for (i = 0; i < a; i++) {
			for(j = 0; j < 6; j++) {
				
				temp[i] = temp[i].replace("{"+prop[j].getKey()+"}",prop[j].getValue());
			}
		}
		
		for (i = 0; i < a; i++) {
			out[i] = temp[i];
		}
				
		try {
					
			BufferedWriter output = new BufferedWriter(new FileWriter("output_file.txt"));
			
			for (i = 0; i < a; i++) {
				
				output.write(out[i]);
				output.newLine();
			}
			output.close();
		} 
		 catch (IOException e)
	    {
	      System.err.println(e);
	      System.exit(1);
	    }


	}
}
