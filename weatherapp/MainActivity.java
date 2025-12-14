package com.example.weatherapp;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity {

    private TextView tvResult;
    private Button btnFetch;
    private ExecutorService executor = Executors.newSingleThreadExecutor();

    // ZMIEŃ NA SWÓJ ADRES IP (127.0.0.1 nie działa z emulatora - bo to jest właśnie ta maszyna)
    // Dla emulatora Android Studio użyj: 10.0.2.2
    private static final String API_URL = "http://10.0.2.2:8000/weather/analysis";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvResult = findViewById(R.id.tvResult);
        btnFetch = findViewById(R.id.btnFetch);

        btnFetch.setOnClickListener(v -> fetchWeatherAnalysis());
    }

    private void fetchWeatherAnalysis() {
        tvResult.setText("Ładowanie...");
        btnFetch.setEnabled(false);

        executor.execute(() -> {
            String result = getDataFromApi();
            runOnUiThread(() -> {
                tvResult.setText(result);
                btnFetch.setEnabled(true);
            });
        });
    }

    private String getDataFromApi() {
        try {
            URL url = new URL(API_URL);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(60000);
            conn.setReadTimeout(60000);

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(conn.getInputStream())
            );
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            return parseResponse(response.toString());

        } catch (Exception e) {
            return "Błąd: " + e.getMessage();
        }
    }

    private String parseResponse(String json) {
        try {
            JSONObject obj = new JSONObject(json);
            StringBuilder sb = new StringBuilder();

            sb.append("Miasto: ").append(obj.getString("city")).append("\n");
            sb.append("Data: ").append(obj.getString("period")).append("\n\n");
            sb.append("Trend: ").append(obj.getString("temperature_trend")).append("\n");
            sb.append("Min: ").append(obj.getDouble("min_temp")).append("'C\n");
            sb.append("Max: ").append(obj.getDouble("max_temp")).append("'C\n\n");
            sb.append("Rekomendacje: ").append(obj.getString("clothing_recommendation")).append("\n\n");

            JSONArray warnings = obj.getJSONArray("warnings");
            if (warnings.length() > 0) {
                sb.append("Ostrzeżenia:\n");
                for (int i = 0; i < warnings.length(); i++) {
                    sb.append("• ").append(warnings.getString(i)).append("\n");
                }
                sb.append("\n");
            }

            sb.append("Podsumowanie: ").append(obj.getString("summary"));

            return sb.toString();

        } catch (Exception e) {
            return "Błąd parsowania: " + e.getMessage();
        }
    }
}