package com.example.fancynotebook.domain.model

import com.example.fancynotebook.data.local.NoteEntity

data class Note(
    val id: Long = 0,
    val title: String,
    val content: String,
    val imageUri: String? = null,
    val createdAt: Long = System.currentTimeMillis(),
    val updatedAt: Long = System.currentTimeMillis()
)

fun NoteEntity.toDomain() = Note(
    id = id,
    title = title,
    content = content,
    imageUri = imageUri,
    createdAt = createdAt,
    updatedAt = updatedAt
)

fun Note.toEntity() = NoteEntity(
    id = id,
    title = title,
    content = content,
    imageUri = imageUri,
    createdAt = createdAt,
    updatedAt = updatedAt
)
