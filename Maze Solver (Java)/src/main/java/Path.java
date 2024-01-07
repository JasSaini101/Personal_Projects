import java.util.ArrayList;
import java.util.NoSuchElementException;


public class Path {

    ArrayList<Square> path;

    public Path(Maze m){
        ArrayList<Square> list = new ArrayList<>();
        list.add(m.getStart());
        path = list;
    }

    public Path(Path p){
        //if (p != null && p.getPath() != null) {

        path = new ArrayList<>(p.getPath());
        //} else {
          //  path = new ArrayList<>();
        //}
    }

    public ArrayList<Square> getPath(){
        return path;
    }

    public int evalPath(Maze m){
        return path.size() + 2*m.evalSquare(path.get(path.size()-1));
    }


    public Path move(Maze m, Direction d) throws UnableToMoveException{
        System.out.println("PATH: " + path);
        Square sq;
        try {
            sq = m.squareAdjacent(path.get(path.size()-1),d);
        } catch (NoSuchElementException e) {
            System.out.println("BOUNDARIES");
            throw new UnableToMoveException();
        }

        if (m.isBlockedSquare(sq)){
            System.out.println("BLOCKED");
            throw new UnableToMoveException();
        }

        Path newPathObject = new Path(this);
        if (!newPathObject.getPath().contains(sq)) newPathObject.push(sq);
        if (newPathObject.isNotRetracing()){
            System.out.println("PATH: " + path);
            return newPathObject;
        } else {
            System.out.println("RETRACING");

            throw new UnableToMoveException();
        }

    }



    /*
public Path move(Maze maze, Direction direction) throws UnableToMoveException {
    Square next;
    try{
        next = maze.squareAdjacent(path.get(path.size()-1),direction);
    }catch(Exception e){
        throw new UnableToMoveException();
    }

    if(maze.isBlockedSquare(next) || !isNotRetracing()){
        throw new UnableToMoveException();
    }

    Path thing = new Path(this);
    thing.getPath().add(next);

    return thing;
}

     */

    public boolean isNotRetracing(){
        /*
        for (Square sq : path){
            if (sq.equals(path.get(path.size()-1)) && sq.hashCode() != path.get(path.size()-1).hashCode()){
                return false;
            }
        }
        return true;

         */
        Square curr = path.get(path.size()-1);
        for (int i=0;i<path.size()-1;i++){
            if (path.get(i).equals(curr)) return false;
        }
        return true;

    }

    public void push(Square sq){
        path.add(sq);
    }
    public void pop(){
        path.remove(path.get(path.size()-1));
    }
    public boolean isSolutionPath(Maze m){
        return path.get(0).equals(m.getStart()) && path.get(path.size()-1).equals(m.getEnd());
    }


    public String getPathString(){
        String s = "";
        for (Square sq : path){
            s += sq.toString() + " ";
        }
        return s;
    }



    public int size(){
        return path.size();
    }

    public String toString(){
        return path.toString();
    }
    public boolean equals(Path other){

        if(path.size() != other.getPath().size()){
            return false;
        }
        for (int i = 0; i < path.size(); i++){
            if (!path.get(i).equals(other.getPath().get(i))){
                return false;
            }
        }
        return true;
    }
}
