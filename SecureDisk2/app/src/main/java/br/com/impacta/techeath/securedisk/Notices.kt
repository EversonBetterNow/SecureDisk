package br.com.impacta.techeath.securedisk

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class Notices {
    var id:Long = 0
    var nome = ""
    var foto = ""

    override fun toString(): String {
        return "Disciplina(nome='$nome')"
    }

}