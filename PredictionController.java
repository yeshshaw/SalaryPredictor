package com.ys.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
public class PredictionController {

    private final RestTemplate restTemplate = new RestTemplate() ;
    @GetMapping("/predict")
    @CrossOrigin(origins = "*")
    public Object predict (@RequestParam double age ) {
        String flaskUrl = "http://127.0.0.1:5000/predict?age=" + age;
       Map<String , Object > respone = restTemplate.getForObject(flaskUrl ,Map.class );
       return  respone ;
    }
}
