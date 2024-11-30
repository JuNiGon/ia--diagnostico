INSERT INTO Doencas (nome, descricao, relevancia) VALUES
('Gripe', 'Infecção viral com sintomas como febre e tosse', 5),
('Resfriado', 'Doença leve das vias respiratórias superiores', 3)
('Pneumonia', 'Infecção pulmonar que causa febre, tosse com catarro e dor no peito', 7),
('Asma', 'Doença crônica que causa dificuldade para respirar e chiado no peito', 6),
('Bronquite', 'Inflamação dos brônquios que causa tosse persistente e falta de ar', 5),
('Sinusite', 'Inflamação dos seios da face que causa dor facial e congestão nasal', 4),
('Dengue', 'Infecção viral transmitida por mosquito com febre alta, dor muscular e manchas vermelhas', 8);

INSERT INTO Sintomas (nome) VALUES
('febre'), ('tosse'), ('coriza'), ('falta de ar'), ('dor no peito'), ('catarro'), ('chiado no peito'),
('congestão nasal'), ('dor facial'), ('dor muscular'), ('manchas vermelhas');

INSERT INTO Doenca_Sintoma (doenca_id, sintoma_id, peso) VALUES
-- Gripe
(1, 1, 10),  
(1, 2, 8),   
-- Resfriado
(2, 3, 7),  
-- Pneumonia;
(3, 1, 9),   
(3, 2, 7),   
(3, 4, 8),
-- Asma
(4, 5, 9),  
(4, 6, 7), 
-- Bronquite
(5, 2, 8),  
(5, 5, 6),  
-- Sinusite
(6, 8, 7),  
(6, 9, 6),  
-- Dengue
(7, 1, 8),  
(7, 10, 9), 
(7, 11, 7); 