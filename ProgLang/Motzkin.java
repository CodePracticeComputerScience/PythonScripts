package ProgLang;

import java.util.ArrayList;
import java.util.Iterator;


public class Motzkin {

	String unaryReturn = new String();
	String binaryReturn = new String();
	ArrayList m = new ArrayList();
	ArrayList l = new ArrayList();
	ArrayList r = new ArrayList();
	public String mot(int n) {
		if( n == 0 ) {
			return "leaf";
		} else {
			m.add(mot(n-1));
			Iterator it = m.iterator();
			while(it.hasNext()) {
			   unaryReturn = "(unary," + it.next().toString() + ")";	
			}
			for( int j=0;j<n-1;j++) {
				l.add(mot(j));
				Iterator it_l = l.iterator();

				r.add(mot(n-2-j));
				Iterator it_r = r.iterator();

				while(it_l.hasNext()) {
					while( it_r.hasNext()) {
						binaryReturn = "(binary," + it_l.next() + "," +  it_r.next() + ")";
					}
				}
			}
			

		}
		yield  unaryReturn + binaryReturn;
		
	}
	/**
	 * @param args
	 */
	public static void main(String args[]) {
//		Iterator it = new Iterator();
		String s = new String();
		for ( int i = 2 ; i <= 3; i++) {
			Motzkin motzkin = new Motzkin();
			s = motzkin.mot(i);
			System.out.println(s);
		}

		
	}
}