package entity;

/**
 * Created by Lzy_pc on 2015/3/16.
 */
public class User {
    private String username;
    public User(){

    }
    public User(String username){
        this.username = username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getUsername() {
        return username;
    }

    @Override
    public String toString() {
        return String.format("User [username %s]\n", this.username);
    }
}
