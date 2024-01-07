import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Iterator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PartialSolutionTest {

    @Test
    void expandPartialSolutionSmallTest() {
        Maze m1 = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        Path p1 = new Path(m1);
        ArrayList<Direction> d1 = new ArrayList<>();
        PartialSolution ps1 = new PartialSolution(d1, p1, m1);
        PSSet psset = ps1.expandPartialSolution(m1);
        assertEquals(1, psset.size());
    }

    @Test
    void expandPartialSolutionRetracingTest() {
        Maze m1 = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        Path p1 = new Path(m1);
        p1.push(new Square(1,1));
        ArrayList<Direction> d1 = new ArrayList<>();
        PartialSolution ps1 = new PartialSolution(d1, p1, m1);
        PSSet psset = ps1.expandPartialSolution(m1);
        assertEquals(1, psset.size());
    }

    @Test
    void expandPartialSolutionThreePathTest() {
        
        Maze m1 = new Maze(3,"[[0,0]]", "[1,1]","[0,1]");
        Path p1 = new Path(m1);
        ArrayList<Direction> d1 = new ArrayList<>();
        PartialSolution ps1 = new PartialSolution(d1, p1, m1);
        System.out.println(ps1);

        PSSet psset = ps1.expandPartialSolution(m1);
        System.out.println(psset);
        assertEquals(4, psset.size());

        d1.add(Direction.LEFT);
        p1.push(new Square(1,0));
        PartialSolution ps2 = new PartialSolution(d1, p1, m1);
        Iterator it1 = psset.iterator();
        while( it1.hasNext())
            System.out.println(it1.next() + ": ");

        assertTrue(psset.contains(ps2));
        
    }

//    Expanding ps1 should result in new PSSet with four partialSolutions
//PSSet:
//PartialSolution{moves=[LEFT], path=Path{[[1,0], [1,1]]}, rating=6}
//PartialSolution{moves=[UP], path=Path{[[0,1], [1,1]]}, rating=2}
//PartialSolution{moves=[DOWN], path=Path{[[2,1], [1,1]]}, rating=3}
//PartialSolution{moves=[RIGHT], path=Path{[[1,2], [1,1]]}, rating=3}


    @Test
    void expandPartialSolutionFourPathTest() {
        
        Maze m1 = new Maze(3,"[]", "[1,1]","[0,1]");
        Path p1 = new Path(m1);
        ArrayList<Direction> d1 = new ArrayList<>();
        PartialSolution ps1 = new PartialSolution(d1, p1, m1);
        System.out.println(ps1);

        PSSet psset = ps1.expandPartialSolution(m1);
        System.out.println(psset);
        assertEquals(4, psset.size());

        d1.add(Direction.LEFT);
        p1.push(new Square(1,0));
        PartialSolution ps2 = new PartialSolution(d1, p1, m1);
        Iterator it1 = psset.iterator();
        while( it1.hasNext())
            System.out.println(it1.next() + ": ");

        assertTrue(psset.contains(ps2));
        
    }

    @Test
    void testEquals() {
        Maze m1 = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        Path p1 = new Path(m1);
        ArrayList<Direction> d1 = new ArrayList<>();
        PartialSolution ps1 = new PartialSolution(d1, p1, m1);
        assertTrue(ps1.equals(ps1));

        Maze m2 = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        Path p2 = new Path(m2);
        ArrayList<Direction> d2 = new ArrayList<>();
        PartialSolution ps2 = new PartialSolution(d2, p2, m2);
        assertTrue(ps1.equals(ps2));
    }
}


