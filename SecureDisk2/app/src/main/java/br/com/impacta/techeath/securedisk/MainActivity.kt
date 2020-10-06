package br.com.impacta.techeath.securedisk

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Gravity
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.core.view.GravityCompat
import com.google.android.material.navigation.NavigationView
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.toolbar.toolbar

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {
    private val context: Context get() = this

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        //setSupportActionBar(toolbar)
        configuraMenuLateral()
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        webView.loadUrl("192.168.15.13:8000/")
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.toolbar, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        val id = item?.itemId

        if(id == R.id.btnEmergencia) {
            startActivity(Intent(this, EmergencyActivity::class.java))
            Toast.makeText(this,"Iniciando chamado de emergência", Toast.LENGTH_LONG).show()
        }
        else if (id == android.R.id.home) {
            if(layoutMenuLateral.isDrawerOpen(Gravity.LEFT))
                layoutMenuLateral.closeDrawer(Gravity.LEFT)
            else
                layoutMenuLateral.openDrawer(Gravity.LEFT)
        }
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

    //ADICIONAIS

    // configuração do navigation Drawer com a toolbar
    private fun configuraMenuLateral() {
    // ícone de menu (hamburger) para mostrar o menu
        var toogle = ActionBarDrawerToggle(
            this,
            layoutMenuLateral,
            toolbar,
            R.string.navigation_drawer_open,
            R.string.navigation_drawer_close)
        layoutMenuLateral.addDrawerListener(toogle)
        toogle.syncState()
        menu_lateral.setNavigationItemSelectedListener(this)
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.nav_noticias -> startActivity(Intent(this, NoticesActivity::class.java))
            R.id.nav_config -> Toast.makeText(this, "Estará disponível em breve aqui na Secure Disk", Toast.LENGTH_SHORT).show()
        }
        // fecha menu depois de tratar o evento
        layoutMenuLateral.closeDrawer(GravityCompat.START)
        return true
    }
}