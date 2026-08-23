package com.example.fancynotebook.data.repository

import com.example.fancynotebook.data.local.NoteDao
import com.example.fancynotebook.domain.model.Note
import com.example.fancynotebook.domain.model.toDomain
import com.example.fancynotebook.domain.model.toEntity
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.withContext
import javax.inject.Inject

class NoteRepository @Inject constructor(
    private val dao: NoteDao,
    private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO
) {

    fun getAllNotes(): Flow<List<Note>> =
        dao.getAll().map { list -> list.map(NoteEntity::toDomain) }

    suspend fun addNote(note: Note) = withContext(ioDispatcher) {
        dao.insert(note.toEntity())
    }

    suspend fun updateNote(note: Note) = withContext(ioDispatcher) {
        dao.update(note.toEntity())
    }

    suspend fun deleteNote(note: Note) = withContext(ioDispatcher) {
        dao.delete(note.toEntity())
    }
}
