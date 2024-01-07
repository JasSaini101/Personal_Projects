public class Square {

    int row;
    int col;

    public Square(int r, int c){
        row = r;
        col = c;
    }
    public Square(){

    }

    public String toString(){
        return "[" + row + "," + col + "]";
    }

    public boolean equals(Square sq2){
        return row == sq2.getRow() && col == sq2.getCol();
    }
    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }


}