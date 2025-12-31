from pydantic import BaseModel, Field

class AnaliseMamografia(BaseModel):
    bi_rads: str = Field(
        description="A classificação BI-RADS final encontrada no laudo (ex: 'Categoria 4', 'BI-RADS 3')."
    )
    lateralidade: str = Field(
        description="A lateralidade da lesão ou achado (ex: 'Esquerda', 'Direita', 'Bilateral', 'Não especificado')."
    )
    resumo_achados: str = Field(
        description="Um resumo breve e técnico dos principais achados que justificam o BI-RADS."
    )