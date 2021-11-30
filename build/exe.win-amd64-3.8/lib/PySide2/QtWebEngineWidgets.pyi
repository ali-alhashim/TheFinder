# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2019 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtWebEngineWidgets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtWebEngineWidgets
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtWebChannel
import PySide2.QtWebEngineCore
import PySide2.QtWebEngineWidgets


class QWebEngineCertificateError(Shiboken.Object):
    CertificateTransparencyRequired: QWebEngineCertificateError = ... # -0xd6
    CertificateValidityTooLong: QWebEngineCertificateError = ... # -0xd5
    CertificateNameConstraintViolation: QWebEngineCertificateError = ... # -0xd4
    CertificateWeakKey       : QWebEngineCertificateError = ... # -0xd3
    CertificateNonUniqueName : QWebEngineCertificateError = ... # -0xd2
    CertificateWeakSignatureAlgorithm: QWebEngineCertificateError = ... # -0xd0
    CertificateInvalid       : QWebEngineCertificateError = ... # -0xcf
    CertificateRevoked       : QWebEngineCertificateError = ... # -0xce
    CertificateUnableToCheckRevocation: QWebEngineCertificateError = ... # -0xcd
    CertificateNoRevocationMechanism: QWebEngineCertificateError = ... # -0xcc
    CertificateContainsErrors: QWebEngineCertificateError = ... # -0xcb
    CertificateAuthorityInvalid: QWebEngineCertificateError = ... # -0xca
    CertificateDateInvalid   : QWebEngineCertificateError = ... # -0xc9
    CertificateCommonNameInvalid: QWebEngineCertificateError = ... # -0xc8
    SslPinnedKeyNotInCertificateChain: QWebEngineCertificateError = ... # -0x96

    class Error(object):
        CertificateTransparencyRequired: QWebEngineCertificateError.Error = ... # -0xd6
        CertificateValidityTooLong: QWebEngineCertificateError.Error = ... # -0xd5
        CertificateNameConstraintViolation: QWebEngineCertificateError.Error = ... # -0xd4
        CertificateWeakKey       : QWebEngineCertificateError.Error = ... # -0xd3
        CertificateNonUniqueName : QWebEngineCertificateError.Error = ... # -0xd2
        CertificateWeakSignatureAlgorithm: QWebEngineCertificateError.Error = ... # -0xd0
        CertificateInvalid       : QWebEngineCertificateError.Error = ... # -0xcf
        CertificateRevoked       : QWebEngineCertificateError.Error = ... # -0xce
        CertificateUnableToCheckRevocation: QWebEngineCertificateError.Error = ... # -0xcd
        CertificateNoRevocationMechanism: QWebEngineCertificateError.Error = ... # -0xcc
        CertificateContainsErrors: QWebEngineCertificateError.Error = ... # -0xcb
        CertificateAuthorityInvalid: QWebEngineCertificateError.Error = ... # -0xca
        CertificateDateInvalid   : QWebEngineCertificateError.Error = ... # -0xc9
        CertificateCommonNameInvalid: QWebEngineCertificateError.Error = ... # -0xc8
        SslPinnedKeyNotInCertificateChain: QWebEngineCertificateError.Error = ... # -0x96

    @typing.overload
    def __init__(self, error:int, url:PySide2.QtCore.QUrl, overridable:bool, errorDescription:str): ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineCertificateError): ...

    def answered(self) -> bool: ...
    def certificateChain(self) -> typing.List: ...
    def defer(self): ...
    def deferred(self) -> bool: ...
    def error(self) -> PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error: ...
    def errorDescription(self) -> str: ...
    def ignoreCertificateError(self): ...
    def isOverridable(self) -> bool: ...
    def rejectCertificate(self): ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QWebEngineContextMenuData(Shiboken.Object):
    MediaTypeNone            : QWebEngineContextMenuData = ... # 0x0
    CanUndo                  : QWebEngineContextMenuData = ... # 0x1
    MediaInError             : QWebEngineContextMenuData = ... # 0x1
    MediaTypeImage           : QWebEngineContextMenuData = ... # 0x1
    CanRedo                  : QWebEngineContextMenuData = ... # 0x2
    MediaPaused              : QWebEngineContextMenuData = ... # 0x2
    MediaTypeVideo           : QWebEngineContextMenuData = ... # 0x2
    MediaTypeAudio           : QWebEngineContextMenuData = ... # 0x3
    CanCut                   : QWebEngineContextMenuData = ... # 0x4
    MediaMuted               : QWebEngineContextMenuData = ... # 0x4
    MediaTypeCanvas          : QWebEngineContextMenuData = ... # 0x4
    MediaTypeFile            : QWebEngineContextMenuData = ... # 0x5
    MediaTypePlugin          : QWebEngineContextMenuData = ... # 0x6
    CanCopy                  : QWebEngineContextMenuData = ... # 0x8
    MediaLoop                : QWebEngineContextMenuData = ... # 0x8
    CanPaste                 : QWebEngineContextMenuData = ... # 0x10
    MediaCanSave             : QWebEngineContextMenuData = ... # 0x10
    CanDelete                : QWebEngineContextMenuData = ... # 0x20
    MediaHasAudio            : QWebEngineContextMenuData = ... # 0x20
    CanSelectAll             : QWebEngineContextMenuData = ... # 0x40
    MediaCanToggleControls   : QWebEngineContextMenuData = ... # 0x40
    CanTranslate             : QWebEngineContextMenuData = ... # 0x80
    MediaControls            : QWebEngineContextMenuData = ... # 0x80
    CanEditRichly            : QWebEngineContextMenuData = ... # 0x100
    MediaCanPrint            : QWebEngineContextMenuData = ... # 0x100
    MediaCanRotate           : QWebEngineContextMenuData = ... # 0x200

    class EditFlag(object):
        CanUndo                  : QWebEngineContextMenuData.EditFlag = ... # 0x1
        CanRedo                  : QWebEngineContextMenuData.EditFlag = ... # 0x2
        CanCut                   : QWebEngineContextMenuData.EditFlag = ... # 0x4
        CanCopy                  : QWebEngineContextMenuData.EditFlag = ... # 0x8
        CanPaste                 : QWebEngineContextMenuData.EditFlag = ... # 0x10
        CanDelete                : QWebEngineContextMenuData.EditFlag = ... # 0x20
        CanSelectAll             : QWebEngineContextMenuData.EditFlag = ... # 0x40
        CanTranslate             : QWebEngineContextMenuData.EditFlag = ... # 0x80
        CanEditRichly            : QWebEngineContextMenuData.EditFlag = ... # 0x100

    class EditFlags(object): ...

    class MediaFlag(object):
        MediaInError             : QWebEngineContextMenuData.MediaFlag = ... # 0x1
        MediaPaused              : QWebEngineContextMenuData.MediaFlag = ... # 0x2
        MediaMuted               : QWebEngineContextMenuData.MediaFlag = ... # 0x4
        MediaLoop                : QWebEngineContextMenuData.MediaFlag = ... # 0x8
        MediaCanSave             : QWebEngineContextMenuData.MediaFlag = ... # 0x10
        MediaHasAudio            : QWebEngineContextMenuData.MediaFlag = ... # 0x20
        MediaCanToggleControls   : QWebEngineContextMenuData.MediaFlag = ... # 0x40
        MediaControls            : QWebEngineContextMenuData.MediaFlag = ... # 0x80
        MediaCanPrint            : QWebEngineContextMenuData.MediaFlag = ... # 0x100
        MediaCanRotate           : QWebEngineContextMenuData.MediaFlag = ... # 0x200

    class MediaFlags(object): ...

    class MediaType(object):
        MediaTypeNone            : QWebEngineContextMenuData.MediaType = ... # 0x0
        MediaTypeImage           : QWebEngineContextMenuData.MediaType = ... # 0x1
        MediaTypeVideo           : QWebEngineContextMenuData.MediaType = ... # 0x2
        MediaTypeAudio           : QWebEngineContextMenuData.MediaType = ... # 0x3
        MediaTypeCanvas          : QWebEngineContextMenuData.MediaType = ... # 0x4
        MediaTypeFile            : QWebEngineContextMenuData.MediaType = ... # 0x5
        MediaTypePlugin          : QWebEngineContextMenuData.MediaType = ... # 0x6

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineContextMenuData): ...

    def __copy__(self): ...
    def editFlags(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlags: ...
    def isContentEditable(self) -> bool: ...
    def isValid(self) -> bool: ...
    def linkText(self) -> str: ...
    def linkUrl(self) -> PySide2.QtCore.QUrl: ...
    def mediaFlags(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlags: ...
    def mediaType(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType: ...
    def mediaUrl(self) -> PySide2.QtCore.QUrl: ...
    def misspelledWord(self) -> str: ...
    def position(self) -> PySide2.QtCore.QPoint: ...
    def selectedText(self) -> str: ...
    def spellCheckerSuggestions(self) -> typing.List: ...


class QWebEngineDownloadItem(PySide2.QtCore.QObject):
    UnknownSaveFormat        : QWebEngineDownloadItem = ... # -0x1
    Attachment               : QWebEngineDownloadItem = ... # 0x0
    DownloadRequested        : QWebEngineDownloadItem = ... # 0x0
    NoReason                 : QWebEngineDownloadItem = ... # 0x0
    SingleHtmlSaveFormat     : QWebEngineDownloadItem = ... # 0x0
    CompleteHtmlSaveFormat   : QWebEngineDownloadItem = ... # 0x1
    DownloadAttribute        : QWebEngineDownloadItem = ... # 0x1
    DownloadInProgress       : QWebEngineDownloadItem = ... # 0x1
    FileFailed               : QWebEngineDownloadItem = ... # 0x1
    DownloadCompleted        : QWebEngineDownloadItem = ... # 0x2
    FileAccessDenied         : QWebEngineDownloadItem = ... # 0x2
    MimeHtmlSaveFormat       : QWebEngineDownloadItem = ... # 0x2
    UserRequested            : QWebEngineDownloadItem = ... # 0x2
    DownloadCancelled        : QWebEngineDownloadItem = ... # 0x3
    FileNoSpace              : QWebEngineDownloadItem = ... # 0x3
    SavePage                 : QWebEngineDownloadItem = ... # 0x3
    DownloadInterrupted      : QWebEngineDownloadItem = ... # 0x4
    FileNameTooLong          : QWebEngineDownloadItem = ... # 0x5
    FileTooLarge             : QWebEngineDownloadItem = ... # 0x6
    FileVirusInfected        : QWebEngineDownloadItem = ... # 0x7
    FileTransientError       : QWebEngineDownloadItem = ... # 0xa
    FileBlocked              : QWebEngineDownloadItem = ... # 0xb
    FileSecurityCheckFailed  : QWebEngineDownloadItem = ... # 0xc
    FileTooShort             : QWebEngineDownloadItem = ... # 0xd
    FileHashMismatch         : QWebEngineDownloadItem = ... # 0xe
    NetworkFailed            : QWebEngineDownloadItem = ... # 0x14
    NetworkTimeout           : QWebEngineDownloadItem = ... # 0x15
    NetworkDisconnected      : QWebEngineDownloadItem = ... # 0x16
    NetworkServerDown        : QWebEngineDownloadItem = ... # 0x17
    NetworkInvalidRequest    : QWebEngineDownloadItem = ... # 0x18
    ServerFailed             : QWebEngineDownloadItem = ... # 0x1e
    ServerBadContent         : QWebEngineDownloadItem = ... # 0x21
    ServerUnauthorized       : QWebEngineDownloadItem = ... # 0x22
    ServerCertProblem        : QWebEngineDownloadItem = ... # 0x23
    ServerForbidden          : QWebEngineDownloadItem = ... # 0x24
    ServerUnreachable        : QWebEngineDownloadItem = ... # 0x25
    UserCanceled             : QWebEngineDownloadItem = ... # 0x28

    class DownloadInterruptReason(object):
        NoReason                 : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x0
        FileFailed               : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x1
        FileAccessDenied         : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x2
        FileNoSpace              : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x3
        FileNameTooLong          : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x5
        FileTooLarge             : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x6
        FileVirusInfected        : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x7
        FileTransientError       : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0xa
        FileBlocked              : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0xb
        FileSecurityCheckFailed  : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0xc
        FileTooShort             : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0xd
        FileHashMismatch         : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0xe
        NetworkFailed            : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x14
        NetworkTimeout           : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x15
        NetworkDisconnected      : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x16
        NetworkServerDown        : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x17
        NetworkInvalidRequest    : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x18
        ServerFailed             : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x1e
        ServerBadContent         : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x21
        ServerUnauthorized       : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x22
        ServerCertProblem        : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x23
        ServerForbidden          : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x24
        ServerUnreachable        : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x25
        UserCanceled             : QWebEngineDownloadItem.DownloadInterruptReason = ... # 0x28

    class DownloadState(object):
        DownloadRequested        : QWebEngineDownloadItem.DownloadState = ... # 0x0
        DownloadInProgress       : QWebEngineDownloadItem.DownloadState = ... # 0x1
        DownloadCompleted        : QWebEngineDownloadItem.DownloadState = ... # 0x2
        DownloadCancelled        : QWebEngineDownloadItem.DownloadState = ... # 0x3
        DownloadInterrupted      : QWebEngineDownloadItem.DownloadState = ... # 0x4

    class DownloadType(object):
        Attachment               : QWebEngineDownloadItem.DownloadType = ... # 0x0
        DownloadAttribute        : QWebEngineDownloadItem.DownloadType = ... # 0x1
        UserRequested            : QWebEngineDownloadItem.DownloadType = ... # 0x2
        SavePage                 : QWebEngineDownloadItem.DownloadType = ... # 0x3

    class SavePageFormat(object):
        UnknownSaveFormat        : QWebEngineDownloadItem.SavePageFormat = ... # -0x1
        SingleHtmlSaveFormat     : QWebEngineDownloadItem.SavePageFormat = ... # 0x0
        CompleteHtmlSaveFormat   : QWebEngineDownloadItem.SavePageFormat = ... # 0x1
        MimeHtmlSaveFormat       : QWebEngineDownloadItem.SavePageFormat = ... # 0x2
    def accept(self): ...
    def cancel(self): ...
    def downloadDirectory(self) -> str: ...
    def downloadFileName(self) -> str: ...
    def id(self) -> int: ...
    def interruptReason(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason: ...
    def interruptReasonString(self) -> str: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isSavePageDownload(self) -> bool: ...
    def mimeType(self) -> str: ...
    def page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def path(self) -> str: ...
    def pause(self): ...
    def receivedBytes(self) -> int: ...
    def resume(self): ...
    def savePageFormat(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat: ...
    def setDownloadDirectory(self, directory:str): ...
    def setDownloadFileName(self, fileName:str): ...
    def setPath(self, path:str): ...
    def setSavePageFormat(self, format:PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat): ...
    def state(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState: ...
    def suggestedFileName(self) -> str: ...
    def totalBytes(self) -> int: ...
    def type(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QWebEngineFullScreenRequest(Shiboken.Object):
    def accept(self): ...
    def origin(self) -> PySide2.QtCore.QUrl: ...
    def reject(self): ...
    def toggleOn(self) -> bool: ...


class QWebEngineHistory(Shiboken.Object):
    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def back(self): ...
    def backItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def backItems(self, maxItems:int) -> typing.List: ...
    def canGoBack(self) -> bool: ...
    def canGoForward(self) -> bool: ...
    def clear(self): ...
    def count(self) -> int: ...
    def currentItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def currentItemIndex(self) -> int: ...
    def forward(self): ...
    def forwardItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def forwardItems(self, maxItems:int) -> typing.List: ...
    def goToItem(self, item:PySide2.QtWebEngineWidgets.QWebEngineHistoryItem): ...
    def itemAt(self, i:int) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def items(self) -> typing.List: ...


class QWebEngineHistoryItem(Shiboken.Object):

    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineHistoryItem): ...

    def __copy__(self): ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    def isValid(self) -> bool: ...
    def lastVisited(self) -> PySide2.QtCore.QDateTime: ...
    def originalUrl(self) -> PySide2.QtCore.QUrl: ...
    def swap(self, other:PySide2.QtWebEngineWidgets.QWebEngineHistoryItem): ...
    def title(self) -> str: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QWebEnginePage(PySide2.QtCore.QObject):
    NoWebAction              : QWebEnginePage = ... # -0x1
    Back                     : QWebEnginePage = ... # 0x0
    FileSelectOpen           : QWebEnginePage = ... # 0x0
    InfoMessageLevel         : QWebEnginePage = ... # 0x0
    NavigationTypeLinkClicked: QWebEnginePage = ... # 0x0
    NormalTerminationStatus  : QWebEnginePage = ... # 0x0
    Notifications            : QWebEnginePage = ... # 0x0
    PermissionUnknown        : QWebEnginePage = ... # 0x0
    WebBrowserWindow         : QWebEnginePage = ... # 0x0
    AbnormalTerminationStatus: QWebEnginePage = ... # 0x1
    FileSelectOpenMultiple   : QWebEnginePage = ... # 0x1
    FindBackward             : QWebEnginePage = ... # 0x1
    Forward                  : QWebEnginePage = ... # 0x1
    Geolocation              : QWebEnginePage = ... # 0x1
    NavigationTypeTyped      : QWebEnginePage = ... # 0x1
    PermissionGrantedByUser  : QWebEnginePage = ... # 0x1
    WarningMessageLevel      : QWebEnginePage = ... # 0x1
    WebBrowserTab            : QWebEnginePage = ... # 0x1
    CrashedTerminationStatus : QWebEnginePage = ... # 0x2
    ErrorMessageLevel        : QWebEnginePage = ... # 0x2
    FindCaseSensitively      : QWebEnginePage = ... # 0x2
    MediaAudioCapture        : QWebEnginePage = ... # 0x2
    NavigationTypeFormSubmitted: QWebEnginePage = ... # 0x2
    PermissionDeniedByUser   : QWebEnginePage = ... # 0x2
    Stop                     : QWebEnginePage = ... # 0x2
    WebDialog                : QWebEnginePage = ... # 0x2
    KilledTerminationStatus  : QWebEnginePage = ... # 0x3
    MediaVideoCapture        : QWebEnginePage = ... # 0x3
    NavigationTypeBackForward: QWebEnginePage = ... # 0x3
    Reload                   : QWebEnginePage = ... # 0x3
    WebBrowserBackgroundTab  : QWebEnginePage = ... # 0x3
    Cut                      : QWebEnginePage = ... # 0x4
    MediaAudioVideoCapture   : QWebEnginePage = ... # 0x4
    NavigationTypeReload     : QWebEnginePage = ... # 0x4
    Copy                     : QWebEnginePage = ... # 0x5
    MouseLock                : QWebEnginePage = ... # 0x5
    NavigationTypeOther      : QWebEnginePage = ... # 0x5
    DesktopVideoCapture      : QWebEnginePage = ... # 0x6
    NavigationTypeRedirect   : QWebEnginePage = ... # 0x6
    Paste                    : QWebEnginePage = ... # 0x6
    DesktopAudioVideoCapture : QWebEnginePage = ... # 0x7
    Undo                     : QWebEnginePage = ... # 0x7
    Redo                     : QWebEnginePage = ... # 0x8
    SelectAll                : QWebEnginePage = ... # 0x9
    ReloadAndBypassCache     : QWebEnginePage = ... # 0xa
    PasteAndMatchStyle       : QWebEnginePage = ... # 0xb
    OpenLinkInThisWindow     : QWebEnginePage = ... # 0xc
    OpenLinkInNewWindow      : QWebEnginePage = ... # 0xd
    OpenLinkInNewTab         : QWebEnginePage = ... # 0xe
    CopyLinkToClipboard      : QWebEnginePage = ... # 0xf
    DownloadLinkToDisk       : QWebEnginePage = ... # 0x10
    CopyImageToClipboard     : QWebEnginePage = ... # 0x11
    CopyImageUrlToClipboard  : QWebEnginePage = ... # 0x12
    DownloadImageToDisk      : QWebEnginePage = ... # 0x13
    CopyMediaUrlToClipboard  : QWebEnginePage = ... # 0x14
    ToggleMediaControls      : QWebEnginePage = ... # 0x15
    ToggleMediaLoop          : QWebEnginePage = ... # 0x16
    ToggleMediaPlayPause     : QWebEnginePage = ... # 0x17
    ToggleMediaMute          : QWebEnginePage = ... # 0x18
    DownloadMediaToDisk      : QWebEnginePage = ... # 0x19
    InspectElement           : QWebEnginePage = ... # 0x1a
    ExitFullScreen           : QWebEnginePage = ... # 0x1b
    RequestClose             : QWebEnginePage = ... # 0x1c
    Unselect                 : QWebEnginePage = ... # 0x1d
    SavePage                 : QWebEnginePage = ... # 0x1e
    OpenLinkInNewBackgroundTab: QWebEnginePage = ... # 0x1f
    ViewSource               : QWebEnginePage = ... # 0x20
    ToggleBold               : QWebEnginePage = ... # 0x21
    ToggleItalic             : QWebEnginePage = ... # 0x22
    ToggleUnderline          : QWebEnginePage = ... # 0x23
    ToggleStrikethrough      : QWebEnginePage = ... # 0x24
    AlignLeft                : QWebEnginePage = ... # 0x25
    AlignCenter              : QWebEnginePage = ... # 0x26
    AlignRight               : QWebEnginePage = ... # 0x27
    AlignJustified           : QWebEnginePage = ... # 0x28
    Indent                   : QWebEnginePage = ... # 0x29
    Outdent                  : QWebEnginePage = ... # 0x2a
    InsertOrderedList        : QWebEnginePage = ... # 0x2b
    InsertUnorderedList      : QWebEnginePage = ... # 0x2c
    WebActionCount           : QWebEnginePage = ... # 0x2d

    class Feature(object):
        Notifications            : QWebEnginePage.Feature = ... # 0x0
        Geolocation              : QWebEnginePage.Feature = ... # 0x1
        MediaAudioCapture        : QWebEnginePage.Feature = ... # 0x2
        MediaVideoCapture        : QWebEnginePage.Feature = ... # 0x3
        MediaAudioVideoCapture   : QWebEnginePage.Feature = ... # 0x4
        MouseLock                : QWebEnginePage.Feature = ... # 0x5
        DesktopVideoCapture      : QWebEnginePage.Feature = ... # 0x6
        DesktopAudioVideoCapture : QWebEnginePage.Feature = ... # 0x7

    class FileSelectionMode(object):
        FileSelectOpen           : QWebEnginePage.FileSelectionMode = ... # 0x0
        FileSelectOpenMultiple   : QWebEnginePage.FileSelectionMode = ... # 0x1

    class FindFlag(object):
        FindBackward             : QWebEnginePage.FindFlag = ... # 0x1
        FindCaseSensitively      : QWebEnginePage.FindFlag = ... # 0x2

    class FindFlags(object): ...

    class JavaScriptConsoleMessageLevel(object):
        InfoMessageLevel         : QWebEnginePage.JavaScriptConsoleMessageLevel = ... # 0x0
        WarningMessageLevel      : QWebEnginePage.JavaScriptConsoleMessageLevel = ... # 0x1
        ErrorMessageLevel        : QWebEnginePage.JavaScriptConsoleMessageLevel = ... # 0x2

    class NavigationType(object):
        NavigationTypeLinkClicked: QWebEnginePage.NavigationType = ... # 0x0
        NavigationTypeTyped      : QWebEnginePage.NavigationType = ... # 0x1
        NavigationTypeFormSubmitted: QWebEnginePage.NavigationType = ... # 0x2
        NavigationTypeBackForward: QWebEnginePage.NavigationType = ... # 0x3
        NavigationTypeReload     : QWebEnginePage.NavigationType = ... # 0x4
        NavigationTypeOther      : QWebEnginePage.NavigationType = ... # 0x5
        NavigationTypeRedirect   : QWebEnginePage.NavigationType = ... # 0x6

    class PermissionPolicy(object):
        PermissionUnknown        : QWebEnginePage.PermissionPolicy = ... # 0x0
        PermissionGrantedByUser  : QWebEnginePage.PermissionPolicy = ... # 0x1
        PermissionDeniedByUser   : QWebEnginePage.PermissionPolicy = ... # 0x2

    class RenderProcessTerminationStatus(object):
        NormalTerminationStatus  : QWebEnginePage.RenderProcessTerminationStatus = ... # 0x0
        AbnormalTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = ... # 0x1
        CrashedTerminationStatus : QWebEnginePage.RenderProcessTerminationStatus = ... # 0x2
        KilledTerminationStatus  : QWebEnginePage.RenderProcessTerminationStatus = ... # 0x3

    class WebAction(object):
        NoWebAction              : QWebEnginePage.WebAction = ... # -0x1
        Back                     : QWebEnginePage.WebAction = ... # 0x0
        Forward                  : QWebEnginePage.WebAction = ... # 0x1
        Stop                     : QWebEnginePage.WebAction = ... # 0x2
        Reload                   : QWebEnginePage.WebAction = ... # 0x3
        Cut                      : QWebEnginePage.WebAction = ... # 0x4
        Copy                     : QWebEnginePage.WebAction = ... # 0x5
        Paste                    : QWebEnginePage.WebAction = ... # 0x6
        Undo                     : QWebEnginePage.WebAction = ... # 0x7
        Redo                     : QWebEnginePage.WebAction = ... # 0x8
        SelectAll                : QWebEnginePage.WebAction = ... # 0x9
        ReloadAndBypassCache     : QWebEnginePage.WebAction = ... # 0xa
        PasteAndMatchStyle       : QWebEnginePage.WebAction = ... # 0xb
        OpenLinkInThisWindow     : QWebEnginePage.WebAction = ... # 0xc
        OpenLinkInNewWindow      : QWebEnginePage.WebAction = ... # 0xd
        OpenLinkInNewTab         : QWebEnginePage.WebAction = ... # 0xe
        CopyLinkToClipboard      : QWebEnginePage.WebAction = ... # 0xf
        DownloadLinkToDisk       : QWebEnginePage.WebAction = ... # 0x10
        CopyImageToClipboard     : QWebEnginePage.WebAction = ... # 0x11
        CopyImageUrlToClipboard  : QWebEnginePage.WebAction = ... # 0x12
        DownloadImageToDisk      : QWebEnginePage.WebAction = ... # 0x13
        CopyMediaUrlToClipboard  : QWebEnginePage.WebAction = ... # 0x14
        ToggleMediaControls      : QWebEnginePage.WebAction = ... # 0x15
        ToggleMediaLoop          : QWebEnginePage.WebAction = ... # 0x16
        ToggleMediaPlayPause     : QWebEnginePage.WebAction = ... # 0x17
        ToggleMediaMute          : QWebEnginePage.WebAction = ... # 0x18
        DownloadMediaToDisk      : QWebEnginePage.WebAction = ... # 0x19
        InspectElement           : QWebEnginePage.WebAction = ... # 0x1a
        ExitFullScreen           : QWebEnginePage.WebAction = ... # 0x1b
        RequestClose             : QWebEnginePage.WebAction = ... # 0x1c
        Unselect                 : QWebEnginePage.WebAction = ... # 0x1d
        SavePage                 : QWebEnginePage.WebAction = ... # 0x1e
        OpenLinkInNewBackgroundTab: QWebEnginePage.WebAction = ... # 0x1f
        ViewSource               : QWebEnginePage.WebAction = ... # 0x20
        ToggleBold               : QWebEnginePage.WebAction = ... # 0x21
        ToggleItalic             : QWebEnginePage.WebAction = ... # 0x22
        ToggleUnderline          : QWebEnginePage.WebAction = ... # 0x23
        ToggleStrikethrough      : QWebEnginePage.WebAction = ... # 0x24
        AlignLeft                : QWebEnginePage.WebAction = ... # 0x25
        AlignCenter              : QWebEnginePage.WebAction = ... # 0x26
        AlignRight               : QWebEnginePage.WebAction = ... # 0x27
        AlignJustified           : QWebEnginePage.WebAction = ... # 0x28
        Indent                   : QWebEnginePage.WebAction = ... # 0x29
        Outdent                  : QWebEnginePage.WebAction = ... # 0x2a
        InsertOrderedList        : QWebEnginePage.WebAction = ... # 0x2b
        InsertUnorderedList      : QWebEnginePage.WebAction = ... # 0x2c
        WebActionCount           : QWebEnginePage.WebAction = ... # 0x2d

    class WebWindowType(object):
        WebBrowserWindow         : QWebEnginePage.WebWindowType = ... # 0x0
        WebBrowserTab            : QWebEnginePage.WebWindowType = ... # 0x1
        WebDialog                : QWebEnginePage.WebWindowType = ... # 0x2
        WebBrowserBackgroundTab  : QWebEnginePage.WebWindowType = ... # 0x3

    @typing.overload
    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...
    @typing.overload
    def __init__(self, profile:PySide2.QtWebEngineWidgets.QWebEngineProfile, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...

    def acceptNavigationRequest(self, url:PySide2.QtCore.QUrl, type:PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType, isMainFrame:bool) -> bool: ...
    def action(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction) -> PySide2.QtWidgets.QAction: ...
    def backgroundColor(self) -> PySide2.QtGui.QColor: ...
    def certificateError(self, certificateError:PySide2.QtWebEngineWidgets.QWebEngineCertificateError) -> bool: ...
    def chooseFiles(self, mode:PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode, oldFiles:typing.Sequence, acceptedMimeTypes:typing.Sequence) -> typing.List: ...
    def contentsSize(self) -> PySide2.QtCore.QSizeF: ...
    def contextMenuData(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData: ...
    def createStandardContextMenu(self) -> PySide2.QtWidgets.QMenu: ...
    def createWindow(self, type:PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def devToolsPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def download(self, url:PySide2.QtCore.QUrl, filename:str=...): ...
    def event(self, arg__1:PySide2.QtCore.QEvent) -> bool: ...
    def findText(self, subString:str, options:PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags=...): ...
    def hasSelection(self) -> bool: ...
    def history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    def inspectedPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def isAudioMuted(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def javaScriptAlert(self, securityOrigin:PySide2.QtCore.QUrl, msg:str): ...
    def javaScriptConfirm(self, securityOrigin:PySide2.QtCore.QUrl, msg:str) -> bool: ...
    def javaScriptConsoleMessage(self, level:PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel, message:str, lineNumber:int, sourceID:str): ...
    def javaScriptPrompt(self, securityOrigin:PySide2.QtCore.QUrl, msg:str, defaultValue:str) -> typing.Tuple: ...
    @typing.overload
    def load(self, request:PySide2.QtWebEngineCore.QWebEngineHttpRequest): ...
    @typing.overload
    def load(self, url:PySide2.QtCore.QUrl): ...
    def printToPdf(self, filePath:str, layout:PySide2.QtGui.QPageLayout=...): ...
    def profile(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile: ...
    def recentlyAudible(self) -> bool: ...
    def replaceMisspelledWord(self, replacement:str): ...
    def requestedUrl(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def runJavaScript(self, scriptSource:str): ...
    @typing.overload
    def runJavaScript(self, scriptSource:str, worldId:int): ...
    def save(self, filePath:str, format:PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat=...): ...
    def scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection: ...
    def scrollPosition(self) -> PySide2.QtCore.QPointF: ...
    def selectedText(self) -> str: ...
    def setAudioMuted(self, muted:bool): ...
    def setBackgroundColor(self, color:PySide2.QtGui.QColor): ...
    def setContent(self, data:PySide2.QtCore.QByteArray, mimeType:str=..., baseUrl:PySide2.QtCore.QUrl=...): ...
    def setDevToolsPage(self, page:PySide2.QtWebEngineWidgets.QWebEnginePage): ...
    def setFeaturePermission(self, securityOrigin:PySide2.QtCore.QUrl, feature:PySide2.QtWebEngineWidgets.QWebEnginePage.Feature, policy:PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy): ...
    def setHtml(self, html:str, baseUrl:PySide2.QtCore.QUrl=...): ...
    def setInspectedPage(self, page:PySide2.QtWebEngineWidgets.QWebEnginePage): ...
    def setUrl(self, url:PySide2.QtCore.QUrl): ...
    def setUrlRequestInterceptor(self, interceptor:PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor): ...
    def setView(self, view:PySide2.QtWidgets.QWidget): ...
    def setVisible(self, visible:bool): ...
    @typing.overload
    def setWebChannel(self, arg__1:PySide2.QtWebChannel.QWebChannel): ...
    @typing.overload
    def setWebChannel(self, arg__1:PySide2.QtWebChannel.QWebChannel, worldId:int): ...
    def setZoomFactor(self, factor:float): ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def title(self) -> str: ...
    def triggerAction(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction, checked:bool=...): ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    def view(self) -> PySide2.QtWidgets.QWidget: ...
    def webChannel(self) -> PySide2.QtWebChannel.QWebChannel: ...
    def zoomFactor(self) -> float: ...


class QWebEngineProfile(PySide2.QtCore.QObject):
    MemoryHttpCache          : QWebEngineProfile = ... # 0x0
    NoPersistentCookies      : QWebEngineProfile = ... # 0x0
    AllowPersistentCookies   : QWebEngineProfile = ... # 0x1
    DiskHttpCache            : QWebEngineProfile = ... # 0x1
    ForcePersistentCookies   : QWebEngineProfile = ... # 0x2
    NoCache                  : QWebEngineProfile = ... # 0x2

    class HttpCacheType(object):
        MemoryHttpCache          : QWebEngineProfile.HttpCacheType = ... # 0x0
        DiskHttpCache            : QWebEngineProfile.HttpCacheType = ... # 0x1
        NoCache                  : QWebEngineProfile.HttpCacheType = ... # 0x2

    class PersistentCookiesPolicy(object):
        NoPersistentCookies      : QWebEngineProfile.PersistentCookiesPolicy = ... # 0x0
        AllowPersistentCookies   : QWebEngineProfile.PersistentCookiesPolicy = ... # 0x1
        ForcePersistentCookies   : QWebEngineProfile.PersistentCookiesPolicy = ... # 0x2

    @typing.overload
    def __init__(self, name:str, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...
    @typing.overload
    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...

    def cachePath(self) -> str: ...
    def clearAllVisitedLinks(self): ...
    def clearHttpCache(self): ...
    def clearVisitedLinks(self, urls:typing.Sequence): ...
    def cookieStore(self) -> PySide2.QtWebEngineCore.QWebEngineCookieStore: ...
    @staticmethod
    def defaultProfile() -> PySide2.QtWebEngineWidgets.QWebEngineProfile: ...
    def downloadPath(self) -> str: ...
    def httpAcceptLanguage(self) -> str: ...
    def httpCacheMaximumSize(self) -> int: ...
    def httpCacheType(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType: ...
    def httpUserAgent(self) -> str: ...
    def installUrlSchemeHandler(self, scheme:PySide2.QtCore.QByteArray, arg__2:PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler): ...
    def isOffTheRecord(self) -> bool: ...
    def isSpellCheckEnabled(self) -> bool: ...
    def isUsedForGlobalCertificateVerification(self) -> bool: ...
    def persistentCookiesPolicy(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy: ...
    def persistentStoragePath(self) -> str: ...
    def removeAllUrlSchemeHandlers(self): ...
    def removeUrlScheme(self, scheme:PySide2.QtCore.QByteArray): ...
    def removeUrlSchemeHandler(self, arg__1:PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler): ...
    def scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection: ...
    def setCachePath(self, path:str): ...
    def setDownloadPath(self, path:str): ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage:str): ...
    def setHttpCacheMaximumSize(self, maxSize:int): ...
    def setHttpCacheType(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType): ...
    def setHttpUserAgent(self, userAgent:str): ...
    def setPersistentCookiesPolicy(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy): ...
    def setPersistentStoragePath(self, path:str): ...
    def setRequestInterceptor(self, interceptor:PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor): ...
    def setSpellCheckEnabled(self, enabled:bool): ...
    def setSpellCheckLanguages(self, languages:typing.Sequence): ...
    def setUrlRequestInterceptor(self, interceptor:PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor): ...
    def setUseForGlobalCertificateVerification(self, enabled:bool=...): ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def spellCheckLanguages(self) -> typing.List: ...
    def storageName(self) -> str: ...
    def urlSchemeHandler(self, arg__1:PySide2.QtCore.QByteArray) -> PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler: ...
    def visitedLinksContainsUrl(self, url:PySide2.QtCore.QUrl) -> bool: ...


class QWebEngineScript(Shiboken.Object):
    Deferred                 : QWebEngineScript = ... # 0x0
    MainWorld                : QWebEngineScript = ... # 0x0
    ApplicationWorld         : QWebEngineScript = ... # 0x1
    DocumentReady            : QWebEngineScript = ... # 0x1
    DocumentCreation         : QWebEngineScript = ... # 0x2
    UserWorld                : QWebEngineScript = ... # 0x2

    class InjectionPoint(object):
        Deferred                 : QWebEngineScript.InjectionPoint = ... # 0x0
        DocumentReady            : QWebEngineScript.InjectionPoint = ... # 0x1
        DocumentCreation         : QWebEngineScript.InjectionPoint = ... # 0x2

    class ScriptWorldId(object):
        MainWorld                : QWebEngineScript.ScriptWorldId = ... # 0x0
        ApplicationWorld         : QWebEngineScript.ScriptWorldId = ... # 0x1
        UserWorld                : QWebEngineScript.ScriptWorldId = ... # 0x2

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineScript): ...

    def __copy__(self): ...
    def injectionPoint(self) -> PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint: ...
    def isNull(self) -> bool: ...
    def name(self) -> str: ...
    def runsOnSubFrames(self) -> bool: ...
    def setInjectionPoint(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint): ...
    def setName(self, arg__1:str): ...
    def setRunsOnSubFrames(self, on:bool): ...
    def setSourceCode(self, arg__1:str): ...
    def setWorldId(self, arg__1:int): ...
    def sourceCode(self) -> str: ...
    def swap(self, other:PySide2.QtWebEngineWidgets.QWebEngineScript): ...
    def worldId(self) -> int: ...


class QWebEngineScriptCollection(Shiboken.Object):
    def clear(self): ...
    def contains(self, value:PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool: ...
    def count(self) -> int: ...
    def findScript(self, name:str) -> PySide2.QtWebEngineWidgets.QWebEngineScript: ...
    def findScripts(self, name:str) -> typing.List: ...
    @typing.overload
    def insert(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineScript): ...
    @typing.overload
    def insert(self, list:typing.Sequence): ...
    def isEmpty(self) -> bool: ...
    def remove(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool: ...
    def size(self) -> int: ...
    def toList(self) -> typing.List: ...


class QWebEngineSettings(Shiboken.Object):
    AutoLoadImages           : QWebEngineSettings = ... # 0x0
    MinimumFontSize          : QWebEngineSettings = ... # 0x0
    StandardFont             : QWebEngineSettings = ... # 0x0
    DisallowUnknownUrlSchemes: QWebEngineSettings = ... # 0x1
    FixedFont                : QWebEngineSettings = ... # 0x1
    JavascriptEnabled        : QWebEngineSettings = ... # 0x1
    MinimumLogicalFontSize   : QWebEngineSettings = ... # 0x1
    AllowUnknownUrlSchemesFromUserInteraction: QWebEngineSettings = ... # 0x2
    DefaultFontSize          : QWebEngineSettings = ... # 0x2
    JavascriptCanOpenWindows : QWebEngineSettings = ... # 0x2
    SerifFont                : QWebEngineSettings = ... # 0x2
    AllowAllUnknownUrlSchemes: QWebEngineSettings = ... # 0x3
    DefaultFixedFontSize     : QWebEngineSettings = ... # 0x3
    JavascriptCanAccessClipboard: QWebEngineSettings = ... # 0x3
    SansSerifFont            : QWebEngineSettings = ... # 0x3
    CursiveFont              : QWebEngineSettings = ... # 0x4
    LinksIncludedInFocusChain: QWebEngineSettings = ... # 0x4
    FantasyFont              : QWebEngineSettings = ... # 0x5
    LocalStorageEnabled      : QWebEngineSettings = ... # 0x5
    LocalContentCanAccessRemoteUrls: QWebEngineSettings = ... # 0x6
    PictographFont           : QWebEngineSettings = ... # 0x6
    XSSAuditingEnabled       : QWebEngineSettings = ... # 0x7
    SpatialNavigationEnabled : QWebEngineSettings = ... # 0x8
    LocalContentCanAccessFileUrls: QWebEngineSettings = ... # 0x9
    HyperlinkAuditingEnabled : QWebEngineSettings = ... # 0xa
    ScrollAnimatorEnabled    : QWebEngineSettings = ... # 0xb
    ErrorPageEnabled         : QWebEngineSettings = ... # 0xc
    PluginsEnabled           : QWebEngineSettings = ... # 0xd
    FullScreenSupportEnabled : QWebEngineSettings = ... # 0xe
    ScreenCaptureEnabled     : QWebEngineSettings = ... # 0xf
    WebGLEnabled             : QWebEngineSettings = ... # 0x10
    Accelerated2dCanvasEnabled: QWebEngineSettings = ... # 0x11
    AutoLoadIconsForPage     : QWebEngineSettings = ... # 0x12
    TouchIconsEnabled        : QWebEngineSettings = ... # 0x13
    FocusOnNavigationEnabled : QWebEngineSettings = ... # 0x14
    PrintElementBackgrounds  : QWebEngineSettings = ... # 0x15
    AllowRunningInsecureContent: QWebEngineSettings = ... # 0x16
    AllowGeolocationOnInsecureOrigins: QWebEngineSettings = ... # 0x17
    AllowWindowActivationFromJavaScript: QWebEngineSettings = ... # 0x18
    ShowScrollBars           : QWebEngineSettings = ... # 0x19
    PlaybackRequiresUserGesture: QWebEngineSettings = ... # 0x1a
    WebRTCPublicInterfacesOnly: QWebEngineSettings = ... # 0x1b
    JavascriptCanPaste       : QWebEngineSettings = ... # 0x1c
    DnsPrefetchEnabled       : QWebEngineSettings = ... # 0x1d
    PdfViewerEnabled         : QWebEngineSettings = ... # 0x1e

    class FontFamily(object):
        StandardFont             : QWebEngineSettings.FontFamily = ... # 0x0
        FixedFont                : QWebEngineSettings.FontFamily = ... # 0x1
        SerifFont                : QWebEngineSettings.FontFamily = ... # 0x2
        SansSerifFont            : QWebEngineSettings.FontFamily = ... # 0x3
        CursiveFont              : QWebEngineSettings.FontFamily = ... # 0x4
        FantasyFont              : QWebEngineSettings.FontFamily = ... # 0x5
        PictographFont           : QWebEngineSettings.FontFamily = ... # 0x6

    class FontSize(object):
        MinimumFontSize          : QWebEngineSettings.FontSize = ... # 0x0
        MinimumLogicalFontSize   : QWebEngineSettings.FontSize = ... # 0x1
        DefaultFontSize          : QWebEngineSettings.FontSize = ... # 0x2
        DefaultFixedFontSize     : QWebEngineSettings.FontSize = ... # 0x3

    class UnknownUrlSchemePolicy(object):
        DisallowUnknownUrlSchemes: QWebEngineSettings.UnknownUrlSchemePolicy = ... # 0x1
        AllowUnknownUrlSchemesFromUserInteraction: QWebEngineSettings.UnknownUrlSchemePolicy = ... # 0x2
        AllowAllUnknownUrlSchemes: QWebEngineSettings.UnknownUrlSchemePolicy = ... # 0x3

    class WebAttribute(object):
        AutoLoadImages           : QWebEngineSettings.WebAttribute = ... # 0x0
        JavascriptEnabled        : QWebEngineSettings.WebAttribute = ... # 0x1
        JavascriptCanOpenWindows : QWebEngineSettings.WebAttribute = ... # 0x2
        JavascriptCanAccessClipboard: QWebEngineSettings.WebAttribute = ... # 0x3
        LinksIncludedInFocusChain: QWebEngineSettings.WebAttribute = ... # 0x4
        LocalStorageEnabled      : QWebEngineSettings.WebAttribute = ... # 0x5
        LocalContentCanAccessRemoteUrls: QWebEngineSettings.WebAttribute = ... # 0x6
        XSSAuditingEnabled       : QWebEngineSettings.WebAttribute = ... # 0x7
        SpatialNavigationEnabled : QWebEngineSettings.WebAttribute = ... # 0x8
        LocalContentCanAccessFileUrls: QWebEngineSettings.WebAttribute = ... # 0x9
        HyperlinkAuditingEnabled : QWebEngineSettings.WebAttribute = ... # 0xa
        ScrollAnimatorEnabled    : QWebEngineSettings.WebAttribute = ... # 0xb
        ErrorPageEnabled         : QWebEngineSettings.WebAttribute = ... # 0xc
        PluginsEnabled           : QWebEngineSettings.WebAttribute = ... # 0xd
        FullScreenSupportEnabled : QWebEngineSettings.WebAttribute = ... # 0xe
        ScreenCaptureEnabled     : QWebEngineSettings.WebAttribute = ... # 0xf
        WebGLEnabled             : QWebEngineSettings.WebAttribute = ... # 0x10
        Accelerated2dCanvasEnabled: QWebEngineSettings.WebAttribute = ... # 0x11
        AutoLoadIconsForPage     : QWebEngineSettings.WebAttribute = ... # 0x12
        TouchIconsEnabled        : QWebEngineSettings.WebAttribute = ... # 0x13
        FocusOnNavigationEnabled : QWebEngineSettings.WebAttribute = ... # 0x14
        PrintElementBackgrounds  : QWebEngineSettings.WebAttribute = ... # 0x15
        AllowRunningInsecureContent: QWebEngineSettings.WebAttribute = ... # 0x16
        AllowGeolocationOnInsecureOrigins: QWebEngineSettings.WebAttribute = ... # 0x17
        AllowWindowActivationFromJavaScript: QWebEngineSettings.WebAttribute = ... # 0x18
        ShowScrollBars           : QWebEngineSettings.WebAttribute = ... # 0x19
        PlaybackRequiresUserGesture: QWebEngineSettings.WebAttribute = ... # 0x1a
        WebRTCPublicInterfacesOnly: QWebEngineSettings.WebAttribute = ... # 0x1b
        JavascriptCanPaste       : QWebEngineSettings.WebAttribute = ... # 0x1c
        DnsPrefetchEnabled       : QWebEngineSettings.WebAttribute = ... # 0x1d
        PdfViewerEnabled         : QWebEngineSettings.WebAttribute = ... # 0x1e
    @staticmethod
    def defaultSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def defaultTextEncoding(self) -> str: ...
    def fontFamily(self, which:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily) -> str: ...
    def fontSize(self, type:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize) -> int: ...
    @staticmethod
    def globalSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def resetAttribute(self, attr:PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute): ...
    def resetFontFamily(self, which:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily): ...
    def resetFontSize(self, type:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize): ...
    def resetUnknownUrlSchemePolicy(self): ...
    def setAttribute(self, attr:PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute, on:bool): ...
    def setDefaultTextEncoding(self, encoding:str): ...
    def setFontFamily(self, which:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily, family:str): ...
    def setFontSize(self, type:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize, size:int): ...
    def setUnknownUrlSchemePolicy(self, policy:PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy): ...
    def testAttribute(self, attr:PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute) -> bool: ...
    def unknownUrlSchemePolicy(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy: ...


class QWebEngineView(PySide2.QtWidgets.QWidget):

    def __init__(self, parent:typing.Optional[PySide2.QtWidgets.QWidget]=...): ...

    def back(self): ...
    def closeEvent(self, arg__1:PySide2.QtGui.QCloseEvent): ...
    def contextMenuEvent(self, arg__1:PySide2.QtGui.QContextMenuEvent): ...
    def createWindow(self, type:PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType) -> PySide2.QtWebEngineWidgets.QWebEngineView: ...
    def dragEnterEvent(self, e:PySide2.QtGui.QDragEnterEvent): ...
    def dragLeaveEvent(self, e:PySide2.QtGui.QDragLeaveEvent): ...
    def dragMoveEvent(self, e:PySide2.QtGui.QDragMoveEvent): ...
    def dropEvent(self, e:PySide2.QtGui.QDropEvent): ...
    def event(self, arg__1:PySide2.QtCore.QEvent) -> bool: ...
    def findText(self, subString:str, options:PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags=...): ...
    def forward(self): ...
    def hasSelection(self) -> bool: ...
    def hideEvent(self, arg__1:PySide2.QtGui.QHideEvent): ...
    def history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def load(self, request:PySide2.QtWebEngineCore.QWebEngineHttpRequest): ...
    @typing.overload
    def load(self, url:PySide2.QtCore.QUrl): ...
    def page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def pageAction(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction) -> PySide2.QtWidgets.QAction: ...
    def reload(self): ...
    def selectedText(self) -> str: ...
    def setContent(self, data:PySide2.QtCore.QByteArray, mimeType:str=..., baseUrl:PySide2.QtCore.QUrl=...): ...
    def setHtml(self, html:str, baseUrl:PySide2.QtCore.QUrl=...): ...
    def setPage(self, page:PySide2.QtWebEngineWidgets.QWebEnginePage): ...
    def setUrl(self, url:PySide2.QtCore.QUrl): ...
    def setZoomFactor(self, factor:float): ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def showEvent(self, arg__1:PySide2.QtGui.QShowEvent): ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def stop(self): ...
    def title(self) -> str: ...
    def triggerPageAction(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction, checked:bool=...): ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    def zoomFactor(self) -> float: ...

# eof
