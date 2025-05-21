# 🧠 Brain Tumor Classifier

Este projeto utiliza **redes neurais convolucionais (CNN)** com Keras e TensorFlow para classificar imagens de ressonância magnética (MRI) de cérebros em quatro categorias:

- Glioma
- Meningioma
- Sem tumor
- Pituitária

## ✅ Acurácia no teste: 91.53%
📉 Perda no teste: 21.35%  

### 🔍 AUC por classe:

- Glioma: 0.99  
- Meningioma: 0.98  
- Sem tumor: 1.00  
- Pituitária: 1.00  

---

## 📁 Estrutura do Projeto

```
brain-tumor-classifier/
│
├── app.py                     # Aplicação Streamlit para upload de imagem e predição
├── brain_tumor.ipynb          # Notebook com todo o pipeline de treinamento e avaliação
├── modelo_brain_tumor.keras   # Modelo treinado salvo
└── README.md                  # Documentação
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/viniciusgarbellini/brain-tumor-classifier.git
cd brain-tumor-classifier
```


### 2. Execute a aplicação
```bash
streamlit run app.py
```

---

## 🖼️ Como Usar

1. Rode a aplicação com o comando acima.
2. Um navegador será aberto automaticamente com a interface.
3. Faça o upload de uma imagem de ressonância (formato `.jpg`, `.jpeg` ou `.png`).
4. A aplicação exibirá a classe do tumor detectado com sua respectiva confiança.

---

## 🤖 Modelo

- Arquitetura baseada em **CNN com camadas de convolução, pooling e dropout**.
- Otimizado com **Adam** e função de perda `categorical_crossentropy`.
- Dataset utilizado: imagens MRI de tumores cerebrais com 4 classes balanceadas.

---

## 👨‍💻 Autor

Desenvolvido por **Vinicius Alef Araujo Cruz**  
**Garbellini**.

---
