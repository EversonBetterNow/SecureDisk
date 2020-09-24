package br.com.impacta.techeath.securedisk

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.toolbar.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
//        setSupportActionBar(toolbar_view)
        webView.loadUrl("192.168.15.13:8000/")
    }
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.toolbar, menu)
//        return true
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        val id = item?.itemId

        if(id == R.id.btnEmergencia)
            startActivity(Intent(this, EmergencyActivity::class.java))
            Toast.makeText(this,"Iniciando chamado de emergência", Toast.LENGTH_LONG).show()
        return super.onOptionsItemSelected(item)
    }

    override fun onBackPressed() {
        // verifica se é possível voltar para
        // uma pagina anterior no WebView
        if (webView.canGoBack()) {
            //volta para pagina anterior
            webView.goBack()
        } else {
            // finaliza atividade
            finish()
        }
    }
}