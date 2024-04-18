package com.example.springelasticsearchproject.config;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class EsConfig {

    @Bean
    public RestHighLevelClient esClient() {
        return new RestHighLevelClient(RestClient.builder(new HttpHost("your_ip", 9200, "http")));
    }
}
