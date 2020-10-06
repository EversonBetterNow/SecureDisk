package br.com.impacta.techeath.securedisk

import android.content.Context

object NoticesService {
    fun getDisciplinas (context: Context): List<Notices> {
        val notices = mutableListOf<Notices>()
        for (i in 1..10) {
            val d = Notices()
            d.nome = "Noticia SecureDisk $i"
            d.foto = "https://lh3.googleusercontent.com/GTmuiIZrppouc6hhdWiocybtRx1Tpbl52eYw4l-nAqHtHd4BpSMEqe-vGv7ZFiaHhG_l4v2m5Fdhapxw9aFLf28ErztHEv5WYIz5fA"
            notices.add(d)
        }
        return notices
    }
}