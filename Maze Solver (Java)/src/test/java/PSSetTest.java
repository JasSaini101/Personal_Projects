import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PSSetTest {

    @Test
    void unionTest() {
        Maze m1 = new Maze(3,"[]", "[1,1]","[0,1]");
        Path p1 = new Path(m1);
        ArrayList<Direction> d1 = new ArrayList<>();
        PartialSolution ps1 = new PartialSolution(d1, p1, m1);

        PSSet psset = ps1.expandPartialSolution(m1);
        System.out.println(psset);
        assertEquals(4, psset.size());

        PSSet psset2 = ps1.expandPartialSolution(m1);
        System.out.println(psset2);
        assertEquals(4, psset2.size());

        PSSet result = PSSet.union(psset, psset2);
        System.out.println(result);
        assertEquals(4, result.size());

//        d1.add(Direction.LEFT);
//        p1.push(new Square(1,0));
//        PartialSolution ps2 = new PartialSolution(d1, p1, m1);
    }

    @Test
    void removeTest() {
    }
}



