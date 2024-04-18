package com.example.springelasticsearchproject.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
public class TestController {

    @GetMapping("/start")
    public String startWeb() {
        return "True";
    }



}
