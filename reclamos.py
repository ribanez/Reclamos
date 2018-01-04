
class reclamos:
    def __init__(self, title, description, keywords, itemreview, summary,
                 date_reclamo, ip_autor, state_rec, reclamo,
                 ip_user, visitas):
        self.title = title
        self.description = description
        self.keywords = keywords
        self.itemreview = itemreview
        self.summary = summary
        self.date_reclamo = date_reclamo
        #self.date_consulta = date_consulta
        self.ip_autor = ip_autor
        self.state_rec = state_rec
        self.reclamo = reclamo
        self.ip_user = ip_user
        self.visitas = visitas