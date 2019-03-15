package com.example.anirbansharma.itravel;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button btn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        btn = (Button) findViewById(R.id.btn);

        btn.setOnClickListener(this);

    }

    public void navToLogin() {
        Intent intent = new Intent(MainActivity.this, dashboard.class);
        startActivity(intent);
    }

    public void sign_in(View view) {
        Intent intent = new Intent(MainActivity.this, sign_in_activity.class);
        startActivity(intent);
    }
    public void onClick(View v){
        if (v == btn){
            navToLogin();
        }
    }


}
