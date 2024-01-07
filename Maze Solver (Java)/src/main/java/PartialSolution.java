import java.util.*;

public class PartialSolution {

    ArrayList<Direction> moves;
    Path path;
    int rating;
    public static int expandCount = 0;


    public PartialSolution(){}
    public PartialSolution(Maze m){
        moves = new ArrayList<>();
        path = new Path(m);
        rating = path.evalPath(m);
    }
    public PartialSolution(ArrayList<Direction> movesList, Path p, Maze m) {
        moves = movesList;
        path = p;
        rating = p.evalPath(m);
    }



    public PSSet expandPartialSolution(Maze m) {
        expandCount++;
        PSSet psSet = new PSSet();
        for (Direction direction: Direction.values()){
            try{
                Path newPath = path.move(m,direction);
                PartialSolution newPS = new PartialSolution(m);
                newPS.moves.addAll(moves);
                newPS.moves.add(direction);
                newPS.path = newPath;
                newPS.rating = newPath.evalPath(m);
                psSet.solutions.add(newPS);

            } catch (UnableToMoveException e){
            }
        }

        return psSet;
    }



    public ArrayList<Direction> getMoves() {
        return moves;
    }

    public Path getPath() {
        return path;
    }

    public void setPath(Path p){
        path = p;
    }

    public int getRating() {
        return rating;
    }

    public boolean isSolution(Maze m) {
        return path.isSolutionPath(m);
    }


    public boolean equals(PartialSolution other) {

        //System.out.println("" + rating + ", " + other.getRating());
        if (!moves.equals(other.getMoves())){
            return false;
        }

        if (!(rating == other.getRating())) {
            return false;
        }

        if (!path.equals(other.getPath())){
            return false;
        }

        return true;
    }

    public String toString(){
        return path.toString();
    }

}
