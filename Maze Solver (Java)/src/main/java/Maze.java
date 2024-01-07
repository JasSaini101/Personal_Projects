import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

public class Maze {

    char[][] grid;
    int size;
    List<Square> blocked;
    Square start;
    Square end;

    public Maze(int s, String b, String st, String e) {
        size = s;
        blocked = parseSquareList(b);
        start = parseSquare(st);
        end = parseSquare(e);
        grid = new char[s][s];
        for (int i = 0; i < s; i++){
            for (int j = 0; j < s; j++){
                Square curSquare = parseSquare("[" + i + "," + j + "]");
                System.out.println(curSquare);
                if (b.contains(curSquare.toString())){
                    grid[i][j] = 'B';
                } else if (curSquare.equals(start)){
                    grid[i][j] = 'S';
                } else if (curSquare.equals(end)){
                    grid[i][j] = 'E';
                } else {
                    grid[i][j] = 'C';
                }
            }
        }
        System.out.println(this);

    }

    public String toString(){
        String s = "";
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                s += (grid[i][j] != 'C') ? grid[i][j] + " " : "_ ";
            }
            s += "\n";
        }
        return s;
        /*
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++){
                Square sq = new Square(i,j);
                if (isBlockedSquare(sq)){
                    s += "B ";
                } else if (isStartPoint(sq)){
                    s += "S ";
                } else if (isEndPoint(sq)){
                    s += "E ";
                } else {
                    s += "_ ";
                }
            }
            s += "\n";
        }
        return s;
        */

    }
    public static Square parseSquare(String s){
        s = s.replaceAll("\\[","").replaceAll("]","").replaceAll(" ","").replaceAll("," , "");
        if (!s.isEmpty()) return new Square(Integer.parseInt(s.substring(0,1)), Integer.parseInt(s.substring(1,2)));
        else return new Square();

    }

    public static ArrayList<Square> parseSquareList(String s){
        ArrayList<Square> newList = new ArrayList<>();
        char[] chars = s.toCharArray();
        boolean hasInts = false;
        for (char c : chars){
            if (Character.isDigit(c)){
                hasInts = true;
            }
        }
        if (hasInts) {
            s = s.replaceAll(" ", "");
            String[] squareArray = s.split(",\\[");


            for (String coords : squareArray) {
                newList.add(parseSquare(coords));
            }
        }
        return newList;

    }


    public int getSize() {
        return size;
    }

    public List<Square> getBlocked() {
        return blocked;
    }

    public Square getStart() {
        return start;
    }

    public Square getEnd() {
        return end;
    }

    public int distance(Square s1, Square s2){
        return Math.abs(s1.getRow() - s2.getRow()) + Math.abs(s1.getCol() - s2.getCol());
    }

    public int countBlockedSquares(Square c1, Square c2){
        int blocked = 0;
        int c1Row = c1.getRow();
        int c2Row = c2.getRow();
        int c1Col = c1.getCol();
        int c2Col = c2.getCol();

        for (int i = Math.min(c1Row,c2Row); i <= Math.max(c1Row,c2Row); i++){
            for (int j = Math.min(c1Col,c2Col); j <= Math.max(c1Col,c2Col); j++) {
                if (grid[i][j] == 'B') blocked++;
            }
        }

        return blocked;
    }

    public int evalSquare(Square sq){
        int blockageFactor = 0;
        int distance = distance(sq, end);
        int amountBlocked = this.countBlockedSquares(sq,end);
        if (2 * amountBlocked > distance){
            blockageFactor = (int) Math.pow(2*amountBlocked-distance,3);
        }


        return distance + blockageFactor;
    }


    public Square squareAdjacent(Square sq, Direction d) throws NoSuchElementException{
        switch (d) {
            case UP:
                if (sq.row - 1 < 0) {
                    throw new NoSuchElementException();
                } else {
                    return new Square(sq.row - 1, sq.col);
                }

            case DOWN:
                if (sq.row + 1 >= size) {
                    throw new NoSuchElementException();
                } else {
                    return new Square(sq.row + 1, sq.col);
                }

            case LEFT:
                if (sq.col - 1 < 0){
                    throw new NoSuchElementException();
                } else {
                    return new Square(sq.row, sq.col - 1);
                }

            case RIGHT:
                if (sq.col + 1 >= size){
                    throw new NoSuchElementException();
                } else {
                    return new Square(sq.row, sq.col + 1);
                }

        }
        return new Square(0,0);
    }

    public boolean isBlockedSquare(Square sq){
        for (Square blockedSquare : blocked){
            if (blockedSquare.equals(sq)){
                return true;
            }
        }
        return false;
    }

    public boolean isEndPoint(Square sq){
        return sq.equals(end);
    }
    public boolean isStartPoint(Square sq){
        return sq.equals(start);
    }
    public static void main(String[] args){
        Maze m1 = new Maze(5, "[[1,2],[1,1],[2,3],[3,3],[1,3],[4,3]]", "[4,0]", "[4,4]");
        List<Direction> ans = Main.solveMaze(m1, 100);
        System.out.println(ans);
        System.out.println(PartialSolution.expandCount);
    }
}