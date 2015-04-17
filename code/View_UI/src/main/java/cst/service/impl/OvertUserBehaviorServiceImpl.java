package cst.service.impl;

import cst.constant.FiveLevelEvaluate;
import cst.dao.UserBehaviorDao;
import cst.entity.DealInfo;
import cst.entity.OvertUserBehavior;
import cst.service.UserBehaviorService;


/**
 * 获取显性行为数据
 * Created by Lzy_pc on 2015/4/16.
 */
public class OvertUserBehaviorServiceImpl implements UserBehaviorService {
    private UserBehaviorDao userBehaviorDao;
    @Override
    public int recieveUserBehavior() {
        return -1;
    }

    /**
     * 收集用户的评论和评分
     * @param overtUserBehavior
     * @return
     */
    public int getOvertBehavior(OvertUserBehavior overtUserBehavior){
        boolean isValid = overtUserBehavior.isvalid();
        if (isValid){
            int reslutCode= -1;
            reslutCode = userBehaviorDao.insertOvertBehavior(overtUserBehavior);
            return reslutCode;
        }
        return -1;
    }

    /**
     * 获取商品的详情
     * @param dealID
     * @return
     */
    public DealInfo getUserDealServer(int dealID){
        return new DealInfo();
    }

    /**
     * 获取用户评分级别
     * @param ID
     * @return
     */
    public FiveLevelEvaluate getUser2ItemGrade(int ID){
        return FiveLevelEvaluate.FIVE_LEVEL;
    }
}
