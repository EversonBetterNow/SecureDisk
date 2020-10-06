package br.com.impacta.techeath.securedisk

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.ProgressBar
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.squareup.picasso.Picasso

class NoticesAdapter (
    val notices: List<Notices>,
    val onClick: (Notices) -> Unit):
    RecyclerView.Adapter<NoticesAdapter.NoticesViewHolder>() {
    // ViewHolder com os elementos da tela
    class NoticesViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val cardNome: TextView
        val cardImg : ImageView
        var cardProgress: ProgressBar
        init {
            cardNome = view.findViewById<TextView>(R.id.cardNome)
            cardImg = view.findViewById<ImageView>(R.id.cardImg)
            cardProgress = view.findViewById<ProgressBar>(R.id.cardProgress)
        }
    }
    // Quantidade de disciplinas na lista
    override fun getItemCount() = this.notices.size
    // inflar layout do adapter
    override fun onCreateViewHolder(
        parent: ViewGroup, viewType: Int): NoticesViewHolder {
        // infla view no adapter
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.adapter_notices, parent, false)
        // retornar ViewHolder
        val holder = NoticesViewHolder(view)
        return holder
    }

    // bind para atualizar Views com os dados
    override fun onBindViewHolder(holder: NoticesViewHolder, position: Int) {
        val context = holder.itemView.context
        // recuperar objeto disciplina
        val notice = notices[position]
        // atualizar dados de disciplina
        holder.cardNome.text = notice.nome
        holder.cardProgress.visibility = View.VISIBLE
        // download da imagem
        Picasso.with(context).load(notice.foto).fit().into(holder.cardImg,

            object: com.squareup.picasso.Callback{
                override fun onSuccess() {
                    holder.cardProgress.visibility = View.GONE
                }
                override fun onError() {
                    holder.cardProgress.visibility = View.GONE
                }
            })

        // adiciona evento de clique
        holder.itemView.setOnClickListener {onClick(notice)}
    }
}
