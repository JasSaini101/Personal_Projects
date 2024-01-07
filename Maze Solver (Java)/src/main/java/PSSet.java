import java.util.*;


class PSComparator implements Comparator<PartialSolution> {
    public int compare(PartialSolution ps1, PartialSolution ps2) {
        if (ps1.getRating() == ps2.getRating()) {
            return ps1.hashCode() - ps2.hashCode();
        } else {
            return ps1.getRating() - ps2.getRating();
        }
    }
}
public class PSSet {
    Set<PartialSolution> solutions = new TreeSet<>(new PSComparator());
    public PSSet(PartialSolution solution) {
        solutions.add(solution);
    }

    public PSSet(Set<PartialSolution> newSolutions) {
        solutions.addAll(newSolutions);
    }
    public PSSet(){}
    public static PSSet union (PSSet s1, PSSet s2) {
        Set<PartialSolution> newList = new TreeSet<>(new PSComparator());
        newList.addAll(s1.getSolutions());
        PSSet newSet = new PSSet(newList);

        for (PartialSolution ps : s2.getSolutions()){
            if (!newSet.contains(ps)){
                newSet.solutions.add(ps);
            }
        }
        return newSet; // Return union of the two instead
    }

    public void remove (PartialSolution toRemove) {
        solutions.remove(toRemove);
    }

    public PartialSolution getBestPartialSolution() {
        int minRating = 0;
        PartialSolution minSolution = new PartialSolution();
        Iterator<PartialSolution> it = solutions.iterator();
        if (it.hasNext()) {
            PartialSolution first = it.next();
            minRating = first.getRating();
            minSolution = first;
        }
        while (it.hasNext()){
            PartialSolution current = it.next();
            if (current.getRating() < minRating){
                minRating = current.getRating();
                minSolution = current;
            }
        }
        return minSolution;
    }

    public int size(){
        return solutions.size();
    }
    public Set<PartialSolution> getSolutions() {
        return solutions;
    }

    public boolean isEmpty(){
        return solutions.isEmpty();
    }


    public boolean contains(PartialSolution ps){
        for (PartialSolution solu : solutions) {
            if (solu.equals(ps)){
                return true;
            }
        }

        return false;
    }

    public String toString(){

        return solutions.toString();
    }


    public Iterator<PartialSolution> iterator(){
        return solutions.iterator();

    }


}
