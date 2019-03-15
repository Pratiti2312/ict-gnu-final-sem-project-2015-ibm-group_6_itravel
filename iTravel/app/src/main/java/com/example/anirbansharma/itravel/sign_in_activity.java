package com.example.anirbansharma.itravel;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class sign_in_activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_in_activity);
    }
    public void join_now(View view) {
        Intent intent = new Intent(sign_in_activity.this, dashboard1.class);
        startActivity(intent);
    }
}
