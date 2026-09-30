/* Catálogo transcrito de Proyecto final.py. Precios en MXN, sin descuentos inventados. */
'use strict';
const PREP = {
 fast:'Ayuno de 8 a 12 horas.',
 nofast:'No requiere ayuno.',
 none:'No requiere preparación previa.',
 urine:'Se recomienda entregar la primera orina de la mañana.',
 lifestyle:'Evitar alcohol, comidas muy grasosas y ejercicio intenso el día previo.',
 meds:'Informar al laboratorio sobre medicamentos o suplementos.',
 ego:'Para el EGO: entregar la primera orina de la mañana o una muestra con al menos 3–4 horas de retención, en frasco estéril, tras aseo genital.',
 period:'Si está menstruando, idealmente posponer el EGO o avisar al laboratorio, ya que puede alterar la muestra.',
 prenatal:'Informar medicamentos, vitaminas prenatales o suplementos.',
 id:'Acudir con identificación y la orden médica, si la institución la solicita.',
 lipidfast:'Ayuno de 9 a 12 horas.',
 alcohol:'Evitar alcohol 24 a 48 horas antes.',
 food:'Evitar comida muy grasosa y ejercicio intenso el día anterior.',
 coffee:'No fumar ni tomar café antes de la toma.',
 lipidmeds:'Informar al laboratorio si usa medicamentos que afectan lípidos, como estatinas, fibratos, anticonceptivos, corticoides o suplementos; no los suspenda sin indicación médica.',
 morning:'Preferiblemente acudir por la mañana y, si se está dando seguimiento, realizar las tomas a una hora similar.',
 biotin:'El código original indica suspender suplementos con biotina 2–3 días antes. Confirma esta indicación con el laboratorio y tu médico antes de modificar su uso.',
 thyroidmeds:'Informar si usa levotiroxina, T3, amiodarona, litio, anticonceptivos, vitaminas o suplementos. No suspenda ningún medicamento sin indicación médica.',
 thyroidfast:'Por lo general, no requiere ayuno.',
 liveralcohol:'Evitar alcohol al menos 48 a 72 horas antes.',
 livermeds:'Informar todos los medicamentos, suplementos y productos herbolarios.',
 liverbhc:'Si también incluye BHC, se toma en la misma visita.',
 psa:'Evite eyaculación y bicicleta/moto/ejercicio intenso 48 h antes.',
 unspecified:'El código original no especifica preparación para este estudio. Confírmala con el laboratorio.'
};
/* Cada registro conserva nombre, precio y recomendaciones de la fuente. */
const CATALOG = [
 {id:'bhc',name:'Biometría hemática',category:'Hematología',price:350,desc:'BHC · Componentes de la sangre.',prep:['nofast'],parts:['bhc'],popular:true},
 {id:'qs6',name:'Química sanguínea de 6 elementos',category:'Química',price:570,desc:'Glucosa, urea, creatinina, ácido úrico, colesterol total y triglicéridos.',prep:['fast'],parts:['glu','urea','cre','acido','col','tri'],popular:true},
 {id:'ego',name:'Examen general de orina',category:'Orina',price:120,desc:'EGO · Análisis de muestra de orina.',prep:['urine'],parts:['ego'],popular:true},
 {id:'basico',name:'Perfil básico',category:'Perfiles',price:680,desc:'Biometría hemática + examen general de orina + química de 6 elementos.',prep:['fast','lifestyle','meds','ego','period'],parts:['bhc','ego','glu','urea','cre','acido','col','tri'],popular:true},
 {id:'lipidico',name:'Perfil lipídico',category:'Perfiles',price:400,desc:'Colesterol total, triglicéridos, HDL, LDL y VLDL.',prep:['lipidfast','alcohol','food','coffee','lipidmeds'],parts:['col','tri','hdl','ldl','vldl']},
 {id:'tiroideo',name:'Perfil tiroideo',category:'Perfiles',price:650,desc:'T3, T4, TSH y anticuerpos anti-Tg.',prep:['morning','biotin','thyroidmeds','thyroidfast'],parts:['t3','t4','tsh','anti']},
 {id:'qs3',name:'Química sanguínea de 3 elementos',category:'Química',price:300,desc:'Glucosa, urea y creatinina.',prep:['fast'],parts:['glu','urea','cre']},
 {id:'qs4',name:'Química sanguínea de 4 elementos',category:'Química',price:400,desc:'Glucosa, urea, creatinina y ácido úrico.',prep:['fast'],parts:['glu','urea','cre','acido']},
 {id:'grupo',name:'Grupo sanguíneo',category:'Hematología',price:250,desc:'Identificación de grupo sanguíneo.',prep:['none'],parts:['grupo']},
 {id:'embarazo-orina',name:'Prueba de embarazo en orina',category:'Hormonas',price:100,desc:'Prueba de embarazo mediante muestra de orina.',prep:['urine'],parts:['emb-orina']},
 {id:'embarazo-sangre',name:'Prueba de embarazo en sangre',category:'Hormonas',price:200,desc:'Prueba de embarazo mediante muestra de sangre.',prep:['unspecified'],parts:['emb-sangre']},
 {id:'embarazo-cuant',name:'Prueba de embarazo cuantitativa',category:'Hormonas',price:500,desc:'Medición cuantitativa para prueba de embarazo.',prep:['unspecified'],parts:['emb-cuant']},
 {id:'glucosa',name:'Glucosa',category:'Química',price:110,desc:'Medición de glucosa en sangre.',prep:['fast'],parts:['glu']},
 {id:'psa',name:'PSA',category:'Otros',price:600,desc:'Antígeno prostático específico.',prep:['psa'],parts:['psa']},
 {id:'hba1c',name:'Hemoglobina glicosilada',category:'Química',price:300,desc:'HbA1c · Estudio de hemoglobina glicosilada.',prep:['nofast'],parts:['hba1c']},
 {id:'embarazada',name:'Perfil de embarazada',category:'Perfiles',price:730,desc:'BHC, EGO, Qs6, prueba de embarazo y grupo sanguíneo.',prep:['fast','urine','prenatal','lifestyle','id'],parts:['bhc','ego','glu','urea','cre','acido','col','tri','emb','grupo']},
 {id:'hepatico',name:'Perfil hepático',category:'Perfiles',price:900,desc:'BHC, bilirrubina total y directa, AST, fosfatasa alcalina, albúmina y proteínas totales.',prep:['fast','liveralcohol','food','livermeds','liverbhc'],parts:['bhc','bil','ast','fos','alb','prot']}
];
