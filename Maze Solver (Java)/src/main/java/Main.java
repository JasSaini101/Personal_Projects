import java.util.ArrayList;

public class Main {
    /*
    public static ArrayList<Direction> solveMaze(Maze m, int runtime) {
        //long time = System.currentTimeMillis();
        PartialSolution p1 = new PartialSolution(new ArrayList<>(),new Path(m),m);
        PSSet set = p1.expandPartialSolution(m);
        PartialSolution bestSol = set.getBestPartialSolution();
        while ((bestSol.getPath() == null || !bestSol.isSolution(m))){
            //time = System.currentTimeMillis();
            set = bestSol.expandPartialSolution(m);
            bestSol = set.getBestPartialSolution();
        }
        return bestSol.getMoves();
    }

     */
    public static ArrayList<Direction> solveMaze(Maze maze, int maxRunTime) throws RuntimeException{
        long start = System.currentTimeMillis();
        PSSet currSet = new PSSet(new PartialSolution(maze));
        PSSet expansion;
        PartialSolution best;
        while(true){
            best=currSet.getBestPartialSolution();
            if (best.isSolution(maze)) {
                return best.getMoves();
            }
            expansion = best.expandPartialSolution(maze);
            currSet = PSSet.union(currSet,expansion);
            currSet.remove(best);
            //System.out.println(System.currentTimeMillis()-start);
            if(System.currentTimeMillis()-start>maxRunTime){
                System.out.println("Max Runtime Exceeded");
                throw new RuntimeException();
            }
        }
    }

}


