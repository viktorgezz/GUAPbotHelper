package com.example.springelasticsearchproject.services;


import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.elasticsearch.action.delete.DeleteRequest;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@Service
public class EsService {

    public static class QuestionEntity {

        private String id;
        private String question;
        private String answer;

        public String getQuestion() {
            return question;
        }

        public void setQuestion(String question) {
            this.question = question;
        }

        public String getAnswer() {
            return answer;
        }

        public void setAnswer(String answer) {
            this.answer = answer;
        }

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }
    }

    private final static String INDEX_NAME = "questions0";

    private final ObjectMapper mapper = new ObjectMapper();

    private final RestHighLevelClient esClient;

    @Autowired
    public EsService(RestHighLevelClient esClient) {
        this.esClient = esClient;
    }

    public void updateQuestion(String id, String question, String answer) {
        QuestionEntity questionEntity = new QuestionEntity();
        questionEntity.setQuestion(question);
        questionEntity.setAnswer(answer);

        IndexRequest indexRequest = new IndexRequest(INDEX_NAME);
        indexRequest.id(id);
        try {
            indexRequest.source(mapper.writeValueAsString(questionEntity), XContentType.JSON);
        } catch (JsonProcessingException e) {
            System.out.println("Error 1");
            throw new RuntimeException(e);
        }

        try {
            esClient.index(indexRequest, RequestOptions.DEFAULT);
        } catch (IOException e) {
            System.out.println("Error 2");
            throw new RuntimeException(e);
        }
    }

    public List<QuestionEntity> search(String searchString) {
        SearchRequest searchRequest = new SearchRequest(INDEX_NAME);
        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
        searchSourceBuilder.query(QueryBuilders.matchQuery("question", searchString).fuzziness("AUTO"));

        searchRequest.source(searchSourceBuilder);
        SearchResponse searchResponse = null;
        try {
            searchResponse = esClient.search(searchRequest, RequestOptions.DEFAULT);
        } catch (IOException e) {
            System.out.println("3");
            throw new RuntimeException(e);
        }

        List<QuestionEntity> questionEntities = new ArrayList<>();
        for (SearchHit hit : searchResponse.getHits().getHits()) {
            Map<String, Object> sourceAsMap = hit.getSourceAsMap();

            QuestionEntity questionEntity = new QuestionEntity();
            questionEntity.setQuestion((String) sourceAsMap.get("question"));
            questionEntity.setAnswer((String) sourceAsMap.get("answer"));
            questionEntities.add(questionEntity);
        }
        return questionEntities;
    }

    public List<QuestionEntity> getAllQuestions() {
        SearchRequest searchRequest = new SearchRequest(INDEX_NAME);
        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
        searchSourceBuilder.query(QueryBuilders.matchAllQuery());
        searchRequest.source(searchSourceBuilder);

        SearchResponse searchResponse;
        try {
            searchResponse = esClient.search(searchRequest, RequestOptions.DEFAULT);
        } catch (IOException e) {
            System.out.println("5");
            throw new RuntimeException(e);
        }

        List<QuestionEntity> questionEntities = new ArrayList<>();
        for (SearchHit hit : searchResponse.getHits().getHits()) {
            Map<String, Object> sourceAsMap = hit.getSourceAsMap();

            QuestionEntity questionEntity = new QuestionEntity();
            questionEntity.setId(hit.getId());
            questionEntity.setQuestion((String) sourceAsMap.get("question"));
            questionEntity.setAnswer((String) sourceAsMap.get("answer"));
            questionEntities.add(questionEntity);
        }

        return questionEntities;
    }

    public void deleteQuestionById(String id) {
        DeleteRequest deleteRequest = new DeleteRequest(INDEX_NAME, id);
        try {
            esClient.delete(deleteRequest, RequestOptions.DEFAULT);
        } catch (IOException e) {
            System.out.println("6");
            throw new RuntimeException(e);
        }
    }
}
