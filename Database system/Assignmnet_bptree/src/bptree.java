import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class bptree {

	private static ArrayList<Node> array = new ArrayList<Node>();
	private static int nodeNum, degree, root = 0, now = 0, key, value, i;
	static String line = "";
	static String comma = ",";
	static String[] temp = new String[3];
	
	public static void main(String[] args) throws IOException {
		
		switch(args[0]) {
		
		case "-c":
			degree = Integer.parseInt(args[2]);
			
			if(degree == 1) {
				System.out.println("error\nDegree cannot be \"1\"");
				return;
			}
			
			BufferedWriter bw = new BufferedWriter(new FileWriter (new File(args[1]))); 
			
			nodeNum = 1;
			bw.write(nodeNum + "\t");
			bw.write(degree+ "\t");
			bw.write(root + "\r\n");
			bw.write("1\t0\t0\t-1\r\n");
			
			bw.close();
			break;
		
		case "-i":
			Node node = new Node();
			
			InputStream in = new FileInputStream(new File(args[1]));
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			
			line = br.readLine();
			temp = line.split("\t");
			
			nodeNum = Integer.parseInt(temp[0]);
			degree = Integer.parseInt(temp[1]);
			root = Integer.parseInt(temp[2]);
			
			in.close();
			br.close();
			
			in = new FileInputStream(new File(args[2]));
			br = new BufferedReader(new InputStreamReader(in));
			
			array = node.take(args[1]);
			while ((line = br.readLine()) != null) {
				temp = line.split(comma);
				
				node = leafNode(Integer.parseInt(temp[0]), 0);
				
				key = Integer.parseInt(temp[0]);
				value = Integer.parseInt(temp[1]);
				
				for(i = 0; i< 2*node.getNum(); i = i + 2) {
					if(node.getPointer().get(i) > key) {
						node.getPointer().add(i, key);
						node.getPointer().add(i+1, value);
						node.setNum(node.getNum() + 1);
						break;
					}
					else if(node.getPointer().get(i) == key)	break;
				}
				
				if(i == 2*node.getNum()) {
					node.getPointer().add(key);
					node.getPointer().add(value);
					node.setNum(node.getNum() + 1);
				}
				
				if(node.getNum() >= degree)		overFlow();
			}
			
			br.close();
			
			Node nodeTemp = new Node();
			
			BufferedWriter bw1 = new BufferedWriter(new FileWriter (new File(args[1]))); 
			
			bw1.write(nodeNum + "\t");
			bw1.write(degree+ "\t");
			bw1.write(root + "\r\n");
			
			for(int i = 0; i<array.size(); i++) {
				nodeTemp = array.get(i);
				bw1.write(nodeTemp.getIsleaf() + "\t");
				bw1.write(nodeTemp.getParent() + "\t");
				bw1.write(nodeTemp.getNum() + "\t");
				for(int j = 0; j<nodeTemp.getPointer().size(); j++) {
					bw1.write(nodeTemp.getPointer().get(j) + "\t");
				}
				bw1.write(nodeTemp.getRight() + "\r\n");
			}
			
			bw1.close();
			break;
	
		case "-d":
			Node node3 = new Node();

			InputStream ind = new FileInputStream(new File(args[1]));
			BufferedReader brd = new BufferedReader(new InputStreamReader(ind));
			
			line = brd.readLine();
			temp = line.split("\t");
			
			nodeNum = Integer.parseInt(temp[0]);
			degree = Integer.parseInt(temp[1]);
			root = Integer.parseInt(temp[2]);
			
			ind.close();
			brd.close();
			
			array = node3.take(args[1]);
			
			ind = new FileInputStream(new File(args[2]));
			brd = new BufferedReader(new InputStreamReader(ind));
		
			while ((line = brd.readLine()) != null) {
				node3 = leafNode(Integer.parseInt(line), 0);
				
				key = Integer.parseInt(line);
				
				for(i = 0; i<2*node3.getNum(); i = i + 2) {
					if(node3.getPointer().get(i) == key) {
						node3.getPointer().remove(i);
						node3.getPointer().remove(i);
						node3.setNum(node3.getNum() - 1);
					}
				}
				
				array.set(now, node3);
				
				if(node3.getNum() <= degree/2 && nodeNum != 1)	underFlow();
			}
			
			brd.close();
			
			Node nodeTemp2 = new Node();
			
			BufferedWriter bw2 = new BufferedWriter(new FileWriter (new File(args[1]))); 
			
			bw2.write(nodeNum + "\t");
			bw2.write(degree+ "\t");
			bw2.write(root + "\r\n");
			
			for(int i = 0; i<array.size(); i++) {
				nodeTemp2 = array.get(i);
				bw2.write(nodeTemp2.getIsleaf() + "\t");
				bw2.write(nodeTemp2.getParent() + "\t");
				bw2.write(nodeTemp2.getNum() + "\t");
				for(int j = 0; j<nodeTemp2.getPointer().size(); j++) {
					bw2.write(nodeTemp2.getPointer().get(j) + "\t");
				}
				bw2.write(nodeTemp2.getRight() + "\r\n");
			}
			
			bw2.close();
			break;
			
		case "-s":
			int s = 0;
			Node node1 = new Node();
			key = Integer.parseInt(args[2]);
			
			InputStream ins = new FileInputStream(new File(args[1]));
			BufferedReader brs = new BufferedReader(new InputStreamReader(ins));
			
			line = brs.readLine();
			temp = line.split("\t");
			
			nodeNum = Integer.parseInt(temp[0]);
			degree = Integer.parseInt(temp[1]);
			root = Integer.parseInt(temp[2]);
			
			ins.close();
			brs.close();
			 
			array = node1.take(args[1]);
			
			node1 = leafNode(key, 1);
			
			for(s = 0; s<2*node1.getNum(); s = s+2) {
				if(node1.getPointer().get(s) == key) {
					System.out.println(node1.getPointer().get(s+1));
					break;
				}
			}
			
			if(s == 2*node1.getNum())	System.out.println("NOT FOUND");
			break;
			
		case "-r":
			int check = 1, r = 0;
			Node node2 = new Node();
			int start = Integer.parseInt(args[2]);
			int end = Integer.parseInt(args[3]);

			InputStream inr = new FileInputStream(new File(args[1]));
			BufferedReader brr = new BufferedReader(new InputStreamReader(inr));
			
			line = brr.readLine();
			temp = line.split("\t");
			
			nodeNum = Integer.parseInt(temp[0]);
			degree = Integer.parseInt(temp[1]);
			root = Integer.parseInt(temp[2]);
			
			inr.close();
			brr.close();
			
			array = node2.take(args[1]);
			
			node2 = leafNode(start, 0);
			
			while(true) {
				for(r = 0; r<2*node2.getNum(); r = r+2) {
					
					if(start <= node2.getPointer().get(r) && node2.getPointer().get(r) <= end)
						System.out.println(node2.getPointer().get(r) + "," + node2.getPointer().get(r+1));
					
					else if(node2.getPointer().get(r) > end) {
						check = 0;
						break;
					}
				}
				if(node2.getRight() == -1 || check == 0) break;
				else		check = node2.getRight();
				
				node2 = array.get(check);
			}
			break;
			
		default:
			System.out.println("error");
			System.out.println("usage: java " + bptree.class.getName()
					+ " [OPTION] [ARGUMENT]");
			break;
		}
	}
	
	public static Node leafNode(int key, int flag){
		Node node = new Node();
		int i = root;
		while(i >= 0){
			now = i;
			node = array.get(i);
			i = node.leaf(key, flag);
		}
		return node;
	}
	
	public static void overFlow() {
		int[] i = new int[2];
		Node node = array.get(now);
		
		i = node.insertSplit(array, nodeNum, degree, now);
		
		nodeNum = i[0];
		if(i[1] >= 0)	root = i[1];
		
		return;
	}
	
	public static void underFlow() {
		Node node = array.get(now);
		int[] a = new int[4];
		int[] b = new int[2];
		
		a = node.merge(array, nodeNum, now);
		nodeNum--;
		
		if(root > now)	root--;
		
		if(a[0] > degree) {
			node = array.get(a[1]);
			b = node.insertSplit(array, nodeNum, degree, a[1]);
			
			nodeNum = b[0];
			
			if(b[1] >= 0)	root = b[1];
		}
		
		if(a[2] == 0 && a[3] == root) {
			node = array.get(root);
			a[3] = node.swapRoot(array, nodeNum, root);
			root = a[3];
			nodeNum--;
		}
		
		if(a[2] < degree/2 && a[3] != root) {
			now = a[3];
			underFlow();
		}
	}
}

class Node{
	
	private ArrayList<Integer> pointer = new ArrayList<Integer>();
	private int isleaf = 1, parent = 0, num = 0, right= -1, i = 0;
	
	public void setNum(int num) {	this.num = num;	}
	public int getIsleaf() {	return isleaf;	}
	public int getParent() {	return parent;	}
	public int getNum() {	return num;	}
	public int getRight() {	return right;	}
	public ArrayList<Integer> getPointer() {	return pointer;	}
	
	public ArrayList<Node> take (String output) throws IOException{
		ArrayList<Node> array = new ArrayList<Node>();
		
		InputStream in = new FileInputStream(new File(output));
		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		
		String line = "";
		
		line = br.readLine();
		while((line = br.readLine()) != null) {
			Node nodeTemp = new Node();
			String[] str = line.split("\t");
			
			nodeTemp.isleaf = Integer.parseInt(str[0]);
			nodeTemp.parent = Integer.parseInt(str[1]);
			nodeTemp.num = Integer.parseInt(str[2]);
			
			for(i = 3; i<(2*nodeTemp.num + 3); i++) 
				nodeTemp.pointer.add(Integer.parseInt(str[i]));
			
			nodeTemp.right = Integer.parseInt(str[i]);
			
			array.add(nodeTemp);
		}
		if(array.isEmpty())	array.add(this);
		
		br.close();
		return array;
	}
	
	public int leaf(int key, int flag) {
		if(isleaf == 1)	return -1;
		
		else if(isleaf == 0) {
			i = right;
			for(int j = 0; j<2*num; j = j+2) {
				if(flag == 1)	System.out.println(pointer.get(j));
				if(pointer.get(j) >= key) {
					i = pointer.get(j+1);
					break;
				}
			}
			return i;
		}
		else		return 0;
	}
	
	public int[]	insertSplit(ArrayList<Node> array, int nodeNum, int degree, int now) {
		Node node1 = new Node();
		Node node2 = new Node();
		Node parNode = new Node();
		Node nowNode = array.get(now);
		
		int parIndex = nowNode.parent;
		int[] i = new int [2];
		int j = 0, key = 0, leftChild = 0, rightChild = 0;
		i[1]= -1;
		
		array.set(now, node1);
		array.add(node2);
		
		node1.isleaf = nowNode.isleaf;
		node2.isleaf = nowNode.isleaf;
		node1.num = (nowNode.num)/2 + (nowNode.num)%2 + nowNode.isleaf -1;
		node2.num = (nowNode.num)/2;
		
		for(j = 0; j<2*node1.num; j++)
			node1.pointer.add(nowNode.pointer.get(j));
		
		for(j = 2*node1.num + 2*(1-nowNode.isleaf); j<nowNode.pointer.size(); j++)
			node2.pointer.add(nowNode.pointer.get(j));
		
		node1.right = nodeNum++;
		node2.right = nowNode.right;
		
		key = nowNode.pointer.get((2*node1.num)-(2*nowNode.isleaf));
		leftChild = now;
		rightChild = node1.right;
		
		if(nowNode.isleaf == 0) {
			Node temp = new Node();
			for(j = 1; j<node2.pointer.size(); j = j + 2){
				temp = array.get(node2.pointer.get(j));
				temp.parent = node1.right;
				array.set(node2.pointer.get(j), temp);
			}
			temp = array.get(node2.right);
			temp.parent = node1.right;
			array.set(node2.right, temp);
			node1.right = nowNode.pointer.get((2*node1.num)-2*nowNode.isleaf + 1);
		}
		
		if(nowNode.parent == now){
			parIndex = nodeNum;
			Node newroot = new Node();
			
			newroot.isleaf = 0;
			newroot.parent = parIndex;
			newroot.num = 0;
			
			array.add(newroot);
			
			i[1] = nodeNum++;
		}
		
		node1.parent = parIndex;
		node2.parent = parIndex;
		i[0] = nodeNum;
		
		parNode = array.get(parIndex);
		
		for(j = 0; j<2*parNode.num; j = j + 2) {
			if(parNode.pointer.get(j) > key) {
				parNode.pointer.add(j, key);
				parNode.pointer.add(j+1, leftChild);
				parNode.pointer.set(j+3, rightChild);
				parNode.num++;
				
				break;
			}
			else if(parNode.pointer.get(j) == key)	break;
		}
		
		if(j >= 2*parNode.num) {
			parNode.pointer.add(key);
			parNode.pointer.add(leftChild);
			parNode.right = rightChild;
			parNode.num++;
		}
		
		if(parNode.num > degree)		i = insertSplit(array, nodeNum, degree, parIndex);
		
		return i;
	}

	public int [] merge(ArrayList<Node> array, int nodeNum, int now) {
		Node parNode = array.get(parent);
		Node node = new Node();
		int sibling = -1;
		int j = 0, k = 0, n = 0;
		int[] i = new int[4];
		
		for(j = 1; j<2*parNode.num; j = j + 2) {
			if(parNode.pointer.get(j) == now) {
				if(j == 1 && parNode.num == 1)	sibling = parNode.right;
				else if(j == 1 && parNode.num != 1)	sibling = parNode.pointer.get(3);
				else if(j != 1)		sibling = parNode.pointer.get(j-2);
				break;
			}
		}
		if(j == 2*parNode.num + 1)	sibling = parNode.pointer.get(j-2);
		
		node = array.get(sibling);
		
		if(isleaf == 1) {
			for(k = 0; k<2*num; k = k + 2) {
				for(n = 0; n<2*node.num; n = n + 2) {
					if(pointer.get(k) < node.pointer.get(n)) {
						node.pointer.add(n, pointer.get(k));
						node.pointer.add(n+1, pointer.get(k+1));
						break;
					}
				}
				if(n == 2*node.num) {
					node.pointer.add(pointer.get(k));
					node.pointer.add(pointer.get(k+1));
				}
			}
			
			node.num = node.num + num;
			
			if(j == 1) {
				Node nodeTemp = new Node();
				for(k = 0; k<nodeNum-1; k++) {
					nodeTemp = array.get(k);
					if(nodeTemp.isleaf == 1 && nodeTemp.right == now)
						nodeTemp.right = sibling;
					array.set(k, nodeTemp);
				}
			}
			
			else		node.right = right;
		}
		
		else {
			int key1 = 0, pointer1 = 0;
			for(k = 1; k<2*parNode.num; k = k + 2) {
				if(j == 1 && parNode.pointer.get(k) == now) {
					key1 = parNode.pointer.get(k-1);
					pointer1 = right;
					node.pointer.add(0, pointer1);
					node.pointer.add(0, key1);
					break;
				}
				else if(j != 1 && parNode.pointer.get(k) == sibling) {
					key1 = parNode.pointer.get(k-1);
					pointer1 = node.right;
					node.right = right;
					node.pointer.add(key1);
					node.pointer.add(pointer1);
					break;
				}
			}
			
			for(k = 0; k<2*num; k = k + 2) {
				for(n = 0; n<2*node.num; n = n + 2) {
					if(pointer.get(k) < node.pointer.get(n)) {
						node.pointer.add(n, pointer.get(k));
						node.pointer.add(n+1, pointer.get(k+1));
						break;
					}
				}
				if(n == 2*node.num) {
					node.pointer.add(pointer.get(k));
					node.pointer.add(pointer.get(k+1));
				}
			}
			
			node.num = node.num + num + 1;
		}
		
		if(j == 1) {
			parNode.pointer.remove(0);
			parNode.pointer.remove(0);
			parNode.num--;
		}
		
		else {
			for(k = 1; k<2*(parNode.num-1); k = k + 2) {
				if(parNode.pointer.get(k) == sibling) {
					parNode.pointer.set(k+2, sibling);
					parNode.pointer.remove(k);
					parNode.pointer.remove(k-1);
					parNode.num--;
				}
			}
			if(parNode.right == now) {
				parNode.right = parNode.pointer.get(2*(parNode.num-1));
				parNode.pointer.remove(2*(parNode.num-1));
				parNode.pointer.remove(2*(parNode.num-2));
				parNode.num--;
			}
		}
		
		array.set(sibling, node);
		array.remove(now);
		
		for(k = 0; k<nodeNum-1; k++) {
			Node nodeTemp = new Node();
			nodeTemp = array.get(k);
			
			if(nodeTemp.right > now)		nodeTemp.right--;
			
			if(nodeTemp.parent == now)	nodeTemp.parent = sibling;
			
			if(nodeTemp.parent > now)	nodeTemp.parent--;
			
			if(nodeTemp.isleaf == 0) {
				for(n = 1; n<2*nodeTemp.num; n = n + 2) {
					if(nodeTemp.pointer.get(n) > now) {
						j = nodeTemp.pointer.get(n) - 1;
						nodeTemp.pointer.set(n, j);
					}
				}
			}
			array.set(k, nodeTemp);
		}
		
		if(sibling > now)	sibling--;
		
		if(parent > now)		parent--;
		
		i[0] = node.num;
		i[1] = sibling;
		i[2] = parNode.num;
		i[3] = parent;
		
		return i;
	}
	
	public int swapRoot(ArrayList<Node> array, int nodeNum, int root) {
		Node node = new Node();
		int newroot = 0;
		 
		node = array.get(root);
		newroot = node.right;
		array.remove(root);
		
		for(i = 0; i<nodeNum -1; i++) {
			node = array.get(i);
			if(node.parent == root)	node.parent = newroot;
			if(node.parent > root)	node.parent--;
			if(node.right > root)	node.right--;
			
			array.set(i, node);
		}
		
		return newroot;
	}
}
