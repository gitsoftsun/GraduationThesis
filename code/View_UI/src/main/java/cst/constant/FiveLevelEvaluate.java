package cst.constant;

/**
 * Created by Lzy_pc on 2015/4/16.
 */
public enum  FiveLevelEvaluate {
    ONE_LEVEL(1), TWO_LEVEL(2), THREE_LEVEL(3), FOUR_LEVEL(4), FIVE_LEVEL(5);
    private int value;
    FiveLevelEvaluate(int value){
        this.value = value;
    }
    public int getValue(){
        return this.value;
    }
}
