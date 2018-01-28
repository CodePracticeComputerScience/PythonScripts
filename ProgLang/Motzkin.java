package javaproject;

import java.util.ArrayList;
import java.util.Iterator;


public class Motzkin {

	String unaryReturn = new String();
	String binaryReturn = new String();
	public String mot(int n) {
		if( n == 0 ) {
			return "leaf";
		} else {
			ArrayList m = new ArrayList();
			m.add(mot(n-1));
			Iterator it = m.iterator();
			while(it.hasNext()) {
			   unaryReturn = unaryReturn + "unary," + it.next().toString();	
			}
			for( int j=0;j<n-1;j++) {
				ArrayList l = new ArrayList();
				l.add(mot(j));
				Iterator it_l = l.iterator();

				ArrayList r = new ArrayList();
				r.add(mot(j));
				Iterator it_r = r.iterator();

				while(it_l.hasNext()) {
					while( it_r.hasNext()) {
						binaryReturn = binaryReturn +  "binary," + it_l.next() + it_r.next();
					}
				}
			}
			

		}
		return unaryReturn + binaryReturn;
		
	}
	public static void main(String args[]) {
//		Iterator it = new Iterator();
		for ( int i = 0 ; i < 6; i++) {
			String s = new String();
			Motzkin motzkin = new Motzkin();
			s = motzkin.mot(i);
			System.out.println(s);
		}

		
	}
}