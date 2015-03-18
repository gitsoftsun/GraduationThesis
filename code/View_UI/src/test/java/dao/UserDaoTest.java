package dao;

import entity.User;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.io.IOException;
import java.io.Reader;
import java.util.Arrays;
import java.util.List;

/**
 * test UserDao
 * Created by Lzy_pc on 2015/3/16.
 */
public class UserDaoTest {
    private UserDao userDao;
    @Test
    public void testInsert() throws IOException{
        String mybatis_config = "dao/mybatis-config.xml";
        Reader reader = Resources.getResourceAsReader(mybatis_config);
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(reader);

        SqlSession sqlSession = sqlSessionFactory.openSession();
        userDao = sqlSession.getMapper(UserDao.class);
        User user = new User("lll");
        System.out.printf("insert status : %s", String.valueOf(userDao.insert(user)));
        sqlSession.commit();
        sqlSession.close();
    }
    @Test
    public void mybatisSpring(){
        ApplicationContext applicationContext;
        String locationConfig = "spring/applicationcontext-mybatis.xml";
        applicationContext = new ClassPathXmlApplicationContext(locationConfig);
        userDao = applicationContext.getBean(UserDao.class);
        List<User> lists = userDao.selectAll();
        for (User user : lists){
            System.out.printf("username : %s\n", user.getUsername());
        }
    }
}
