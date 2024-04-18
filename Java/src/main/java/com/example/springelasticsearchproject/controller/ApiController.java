package com.example.springelasticsearchproject.controller;

import com.example.springelasticsearchproject.services.EsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/apis")
public class ApiController {

    private final EsService esService;

    @Autowired
    public ApiController(EsService esService) {
        this.esService = esService;
    }

    @PutMapping("/question_add")
    public String addQuestion(@RequestParam("question") String question,
                              @RequestParam("answer") String answer) {
        String id = UUID.randomUUID().toString();
        esService.updateQuestion(id, question, answer);
        return id;
    }

    @GetMapping("/search/{field}")
    public List<EsService.QuestionEntity> search(@PathVariable("field") String field) {
        return esService.search(field);
    }

    @GetMapping("/get_all")
    public List<EsService.QuestionEntity> matchAll() {
        return esService.getAllQuestions();
    }

    @DeleteMapping("/delete/{id}")
    public void deleteQuestion(@PathVariable("id") String id) {
        esService.deleteQuestionById(id);
    }
}
