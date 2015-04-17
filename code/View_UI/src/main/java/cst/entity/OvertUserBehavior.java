package cst.entity;

import cst.constant.FiveLevelEvaluate;

/**
 * Created by Lzy_pc on 2015/4/16.
 */
public class OvertUserBehavior {
    private int id;
    private int dealID;
    private String evaluateContent;
    private FiveLevelEvaluate sameItemDescGrade;

    public boolean isvalid(){
        if (this.dealID != 0){
            return true;
        }
        return false;
    }
    public void setDealID(int dealID) {
        this.dealID = dealID;
    }

    public int getId() {
        return id;
    }

    public int getDealID() {
        return dealID;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setEvaluateContent(String evaluateContent) {
        this.evaluateContent = evaluateContent;
    }

    public FiveLevelEvaluate getSameItemDescGrade() {
        return sameItemDescGrade;
    }

    public void setSameItemDescGrade(FiveLevelEvaluate sameItemDescGrade) {
        this.sameItemDescGrade = sameItemDescGrade;
    }

    public String getEvaluateContent() {
        return evaluateContent;
    }
}
