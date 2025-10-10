CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('usuario_final', 'lugar_privado') NOT NULL,  -- Diferencia actores
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,  -- Usa bcrypt en FastAPI
    nombre VARCHAR(255) NOT NULL,
    perfil_tags JSON,  -- Para personalidad: ej. {"extrovertido": true, "aventurero": 0.8}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lugar_id INT NOT NULL,  -- FK a usuarios (lugar_privado)
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    es_masivo BOOLEAN DEFAULT FALSE,  -- Marca para eventos masivos
    capacidad INT,  -- Para limitados
    fecha_inicio DATETIME NOT NULL,
    fecha_fin DATETIME NOT NULL,
    perfil_tags JSON,  -- Para matching con usuarios: ej. {"cultural": true, "sostenible": 0.9}
    nft_cantidad INT DEFAULT 0,  -- Boletas como NFTs
    nft_rango_precio DECIMAL(10,2),  -- Para masivos: rangos de precios
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lugar_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    evento_id INT NOT NULL,
    nft_token_id VARCHAR(255),  -- ID del NFT en Avalanche (más adelante)
    estado ENUM('reservado', 'usado', 'cancelado') DEFAULT 'reservado',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE
);

CREATE TABLE recomendaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo ENUM('ruta_turistica', 'evento') NOT NULL,
    contenido JSON,  -- Ej. para ruta: {"sitios": ["Parque X", "Café Y"], "duracion": "2h"}
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);