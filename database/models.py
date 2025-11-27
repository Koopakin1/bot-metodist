from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class User:
    """
    Модель пользователя
    """
    id: Optional[int] = None
    telegram_id: Optional[int] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    referral_code: Optional[str] = None
    referred_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: bool = True
    is_blocked: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        ""Преобразование модели в словарь"""
        return {
            'id': self.id,
            'telegram_id': self.telegram_id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'referral_code': self.referral_code,
            'referred_by': self.referred_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active,
            'is_blocked': self.is_blocked
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        ""Создание модели из словаря"""
        return cls(
            id=data.get('id'),
            telegram_id=data.get('telegram_id'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            referral_code=data.get('referral_code'),
            referred_by=data.get('referred_by'),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            updated_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None,
            is_active=data.get('is_active', True),
            is_blocked=data.get('is_blocked', False)
        )


@dataclass
class Referral:
    """
    Модель реферала
    """
    id: Optional[int] = None
    referrer_id: Optional[int] = None
    referred_id: Optional[int] = None
    created_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование модели в словарь"""
        return {
            'id': self.id,
            'referrer_id': self.referrer_id,
            'referred_id': self.referred_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Referral':
        """Создание модели из словаря"""
        return cls(
            id=data.get('id'),
            referrer_id=data.get('referrer_id'),
            referred_id=data.get('referred_id'),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None
        )


@dataclass
class File:
    """
    Модель файла
    """
    id: Optional[int] = None
    user_id: Optional[int] = None
    file_path: Optional[str] = None
    file_name: Optional[str] = None
    file_size: Optional[int] = None
    file_type: Optional[str] = None
    uploaded_at: Optional[datetime] = None
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование модели в словарь"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'file_path': self.file_path,
            'file_name': self.file_name,
            'file_size': self.file_size,
            'file_type': self.file_type,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None,
            'is_active': self.is_active
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'File':
        ""Создание модели из словаря"""
        return cls(
            id=data.get('id'),
            user_id=data.get('user_id'),
            file_path=data.get('file_path'),
            file_name=data.get('file_name'),
            file_size=data.get('file_size'),
            file_type=data.get('file_type'),
            uploaded_at=datetime.fromisoformat(data['uploaded_at']) if data.get('uploaded_at') else None,
            is_active=data.get('is_active', True)
        )


@dataclass
class Program:
    """
    Модель программы
    """
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    content_path: Optional[str] = None
    duration: Optional[int] = None  # в минутах
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        ""Преобразование модели в словарь"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'content_path': self.content_path,
            'duration': self.duration,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Program':
        ""Создание модели из словаря"""
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
            content_path=data.get('content_path'),
            duration=data.get('duration'),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            updated_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None,
            is_active=data.get('is_active', True)
        )


@dataclass
class BaseModel:
    ""
    Базовая модель для всех моделей
    """
    id: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование модели в словарь"""
        raise NotImplementedError
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """Создание модели из словаря"""
        raise NotImplementedError