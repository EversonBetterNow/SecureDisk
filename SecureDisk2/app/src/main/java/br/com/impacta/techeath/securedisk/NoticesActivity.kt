package br.com.impacta.techeath.securedisk

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.recyclerview.widget.DefaultItemAnimator
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_notices.*

class NoticesActivity : AppCompatActivity() {
    private val context: Context get() = this
    private var notices = listOf<Notices>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_notices)

        recyclerNotices?.layoutManager = LinearLayoutManager(context)
        recyclerNotices?.itemAnimator = DefaultItemAnimator()
        recyclerNotices?.setHasFixedSize(true)
    }

    override fun onResume() {
        super.onResume()
        // task para recuperar as disciplinas
        taskNotices()
    }
    fun taskNotices() {
        notices = NoticesService.getDisciplinas(context)
        // atualizar lista
        recyclerNotices?.adapter = NoticesAdapter(notices) {onClickNotices(it)}
    }

    fun onClickNotices(notice: Notices) {
        Toast.makeText(context, "Clicou disciplina ${notice.nome}", Toast.LENGTH_SHORT).show()
    }
}