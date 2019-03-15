package com.example.anirbansharma.itravel;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class dashboard1 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard1);
    }
    public void sign_in(View view)

    {
        Intent intent = new Intent(dashboard1.this, map_activity.class);
        startActivity(intent);
    }
}
