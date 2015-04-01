package cst.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;


/**
 * Created by Lzy_pc on 2015/3/19.
 */
@Controller
@RequestMapping("/cst/hello")
public class HelloController {
    @RequestMapping({"/"})
    public String printWelcome(ModelMap model){
        model.addAttribute("message", "spring 3 mvc");
        return "hello";
    }
}
