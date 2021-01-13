package com.example.weatherapp01;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    AutoCompleteTextView editText;
    Button button,button1;
    ImageView imageview;
    TextView  country,city,temp,humidity,sunrise,sunset,pressure;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editText = findViewById(R.id.autoCompleteTextView);
        button = findViewById(R.id.button);
        country = findViewById(R.id.country);
        city=findViewById(R.id.city);
        temp=findViewById(R.id.textView5);
        humidity=findViewById(R.id.Humidity);
        sunrise=findViewById(R.id.textView12);
        sunset=findViewById(R.id.Sunset);
        pressure=findViewById(R.id.Pressure);



        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                findWeather();
            }
        });



    }
            public void findWeather(){

        String city_name =editText.getText().toString();
        String url ="http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=37d792f7e63e89331866bc672fe6ab64";

                StringRequest stringrequest = new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        try {
                            JSONObject jsonObject = new JSONObject(response);

                            JSONObject object1 = jsonObject.getJSONObject("sys");
                            String country_find = object1.getString("country");
                            country.setText(country_find);

                            //city
                            String city_find = jsonObject.getString("name");
                            city.setText(city_find);

                            //temperature
                            JSONObject object2 = jsonObject.getJSONObject("main");
                            String temp_find = object2.getString("temp");
                            temp.setText(" "+temp_find+" °C");

                            //image icon
                            //JSONArray jsonArray = jsonObject.getJSONArray("weather");
                            //JSONObject jsonObject1 = jsonArray.getJSONObject(0);
                           // String img = jsonObject1.getString("icon");


                            //Picasso.get().load("http://openweathermap.org/img/wn/"+img+"@2x.png").into(imageview);

                            //humididty
                            JSONObject object3 = jsonObject.getJSONObject("main");
                            String humidity_find = object3.getString("humidity");
                            humidity.setText(humidity_find+" %");


                            //humididty
                            JSONObject object4 = jsonObject.getJSONObject("sys");
                            String sunrise_find = object4.getString("sunrise");
                            sunrise.setText(sunrise_find);

                            //sunset
                            JSONObject object5 = jsonObject.getJSONObject("sys");
                            String sunset_find = object5.getString("sunset");
                            sunset.setText(sunset_find);

                            //pressure
                            JSONObject object6 = jsonObject.getJSONObject("main");
                            String pressure_find = object6.getString("pressure");
                            pressure.setText(pressure_find+" hPa");


                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                        Toast.makeText(MainActivity.this,error.getLocalizedMessage(),Toast.LENGTH_SHORT).show();

                    }
                });

                RequestQueue requestQueue = Volley.newRequestQueue(MainActivity.this);
                requestQueue.add(stringrequest);



            }


}