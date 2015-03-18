package dao;

import entity.User;

import java.util.List;

/**
 * Created by Lzy_pc on 2015/3/16.
 */
public interface UserDao {
    public int insert(User user);
    public List<User> selectAll();

}
